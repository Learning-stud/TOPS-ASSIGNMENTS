import React, { useState } from 'react'
import axios from 'axios'
import { toast } from 'react-toastify'
import { Link, redirect, useNavigate } from 'react-router-dom'
export default function SignUp() {
  const redirect = useNavigate();

  const [formvalue, setFormvalue] = useState({

    email: "",
    password: ""

  });


  const onchange = (e) => {
    setFormvalue({ ...formvalue, [e.target.name]: e.target.value });
    console.log(formvalue)
  }
  function validation() {

    var result = true;

    if (formvalue.email == "") {
      toast.error('Email Field is required !');
      result = false;
    }

    if (formvalue.password == "") {
      toast.error('Password Field is required !');
      result = false;
    }
    return result;
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (validation()) {
      const result = await axios.get(`http://localhost:3000/usertable?email=${formvalue.email}`);
      console.log(result)
      if (result.data.length > 0) {
        if (result.data[0].password == formvalue.password) {
          localStorage.setItem('username', result.data[0].name);
          localStorage.setItem('userid', result.data[0].id);

          toast.success('Login Success !');
          redirect('/')
        }
        else {
          toast.error('Login nai thai jato re !');
        }

      } else {
        toast.error('Login nai thai jato re !');
      }
    }
  }
  return (
    <div>
      <div className="contact_section layout_padding">
        <div className="container">
          <h1 className="contact_text">Login</h1>
        </div>
      </div>
      <div className="contact_section_2 layout_padding">
        <div className="container-fluid">
          <div className="row">
            <div className="col-md-6 padding_0">
              <div className="mail_section">
                <div className="email_text">
                  <div className="form-group">
                  </div>
                  <div className="form-group">
                    <input type="email" value={formvalue.email} onChange={onchange} name="email" className="email-bt" placeholder="Email" />
                  </div>
                  <div className="form-group">
                  </div>
                  <div className="form-group">
                    <input type="password" value={formvalue.password} onChange={onchange} name="password" className="email-bt" placeholder=" password" />
                  </div>

                  <div className="send_btn">
                    <button type="submit" className="btn btn-info" onClick={handleSubmit}>Login</button>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>

  )
}
