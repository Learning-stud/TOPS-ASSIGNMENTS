import React from 'react'

function Service() {
  return (
  <div><div className="services_section layout_padding">
    <div className="container">
      <div className="row">
        <div className="col-sm-12">
          <h1 className="services_taital">Services</h1>
          <p className="services_text">Typesetting industry lorem Ipsum is simply dummy text of the </p>
        </div>
      </div>
      <div className="services_section_2">
        <div className="row">
          <div className="col-lg-4 col-sm-12 col-md-4">
            <div className="box_main active">
              <div className="house_icon">
                <img src="images/icon1.png" className="image_1" />
                <img src="images/icon1.png" className="image_2" />
              </div>
              <h3 className="decorate_text">Original Coffee</h3>
              <p className="tation_text">Exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea </p>
              <div className="readmore_bt"><a href="#">Read More</a></div>
            </div>
          </div>
          <div className="col-lg-4 col-sm-12 col-md-4">
            <div className="box_main">
              <div className="house_icon">
                <img src="images/icon2.png" className="image_1" />
                <img src="images/icon2.png" className="image_2" />
              </div>
              <h3 className="decorate_text">20 Coffee Flavors</h3>
              <p className="tation_text">Exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea </p>
              <div className="readmore_bt"><a href="#">Read More</a></div>
            </div>
          </div>
          <div className="col-lg-4 col-sm-12 col-md-4">
            <div className="box_main">
              <div className="house_icon">
                <img src="images/icon3.png" className="image_1" />
                <img src="images/icon3.png" className="image_2" />
              </div>
              <h3 className="decorate_text">Pleasant Abient</h3>
              <p className="tation_text">Exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea </p>
              <div className="readmore_bt"><a href="#">Read More</a></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div></div>

  )
}

export default Service