import React, { useState } from 'react'
import axios from 'axios'
import { toast } from 'react-toastify'
export default function SignUp() {

  const [formvalue, setFormvalue] = useState({
    name: "",
    email: "",
    phoneNo: "",
    password: ""

  });


  const onchange = (e) => {
    setFormvalue({ ...formvalue, id: new Date().getTime().toString(), [e.target.name]: e.target.value });
    console.log(formvalue)
  }
  function validation() {

    var result = true;
    if (formvalue.name == "") {
      toast.error('Name Field is required !');
      result = false;
    }
    if (formvalue.email == "") {
      toast.error('Email Field is required !');
      result = false;
    }
    if (formvalue.phoneNo == "") {
      toast.error('Phone No Field is required !');
      result = false;
    }
    if (formvalue.password == "") {
      toast.error('Password Field is required !');
      result = false;
    }
    return result;
  }

  const onsubmit = async (e) => {
    e.preventDefault();
    if (validation()) {
      const result = await axios.post(`http://localhost:3000/usertable`, formvalue);
      if (result.status = 201) {
        toast.success('Inquiry  Subbmitted Success');
        setFormvalue({ ...formvalue, name: "", email: "", phoneNo: "", password: "" });
      }
    }
  }
  return (
    <div>
      <div className="contact_section layout_padding">
        <div className="container">
          <h1 className="contact_text">Contact Us</h1>
        </div>
      </div>
      <div className="contact_section_2 layout_padding">
        <div className="container-fluid">
          <div className="row">
            <div className="col-md-6 padding_0">
              <div className="mail_section">
                <div className="email_text">
                  <div className="form-group">
                    <input type="text" value={formvalue.name} onChange={onchange} name="name" className="email-bt" placeholder="Name" />
                  </div>
                  <div className="form-group">
                    <input type="email" value={formvalue.email} onChange={onchange} name="email" className="email-bt" placeholder="Email" />
                  </div>
                  <div className="form-group">
                    <input type="number" value={formvalue.phoneNo} onChange={onchange} name="phoneNo" className="email-bt" placeholder="Phone Numbar" />
                  </div>
                  <div className="form-group">
                    <input type="password" value={formvalue.password} onChange={onchange} name="password" className="email-bt" placeholder=" password" />
                  </div>

                  <div className="send_btn">
                    <div type="text" onClick={onsubmit} className="main_bt"><a href="#">SEND</a></div>
                  </div>
                </div>
              </div>
            </div>
            <div className="col-md-6 padding_0">
              <div className="map-responsive">
                <iframe src="https://www.google.com/maps/embed/v1/place?key=AIzaSyA0s1a7phLN0iaD6-UE7m4qP-z21pH0eSc&q=Eiffel+Tower+Paris+France" width={600} height={508} frameBorder={0} style={{ border: 0, width: '100%' }} allowFullScreen />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  )
}
