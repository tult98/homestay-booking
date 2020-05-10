import React, { Component } from "react";
import axios from "axios";
import "./Header.css";
// import for routing
import { Link } from "react-router-dom";

class Header extends Component {
  render() {
    return (
      <div className="header">
        <div className="">
          <h1>
            <Link className="title" to={"/"}>
              Homestay Booking
            </Link>
          </h1>
        </div>

        <div className="menu">
          <Link className="login" to={"/login"}>
            Đăng nhập
          </Link>
          <Link className="signup" to={"/register"}>
            Đăng ký
          </Link>
        </div>
      </div>
    );
  }
}

export default Header;
