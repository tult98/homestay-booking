import React, { Component } from "react";
import axios from "axios";
import "./Header.css";
// import for routing
import { Link } from "react-router-dom";
import authService from "../services/auth.service";

class Header extends Component {
  state = {
    currentUser: undefined
  };

  componentDidMount() {
    const user = authService.getCurrentUser();

    if(user) {
      this.setState({
        currentUser: user
      });
      console.log(user)
    }
  }

  logOut() {
    authService.logout();
  }

  render() {
    const {currentUser} = this.state;

    return (
      <div className="header">
        <div className="">
          <h1>
            <Link className="title" to={"/"}>
              Homestay Booking
            </Link>
          </h1>
        </div>

        
        {currentUser ? (
          <div className="menu">
            <div className="user">
              {currentUser.user.email}
            </div>
            <div className="menu">
              <a href="/" className="signup" onClick={this.logOut}>
                LogOut
              </a>
            </div>
          </div>
            ) : (
              <div className="menu">
                <Link to={"/login"} className="login">
                  Login
                </Link>
                <Link to={"/register"} className="signup">
                  Sign Up
                </Link>
              </div>
            )}
      </div>
    );
  }
}

export default Header;
