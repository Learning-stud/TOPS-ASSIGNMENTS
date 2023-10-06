import React from 'react'
import { NavLink } from 'react-router-dom'

function Header() {
  return (

<div className="header_section">
  <div className="container-fluid">
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="logo"><a href="index.html"><img src="images/logo.png" /></a></div>
      <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon" />
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav ml-auto">
          <li className="nav-item">
            <NavLink className="nav-link" to="/">Home</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/About">About Us</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/Ourgallery">Gallery</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/Service">Services</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/SignUp">Sign Up</NavLink>
          </li> 
          <li className="nav-item">
            <NavLink className="nav-link" to="/Login">login</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/UserProfile">User Profile</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="#"><i className="fa fa-search" aria-hidden="true" /></NavLink>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</div>

  )
}

export default Header