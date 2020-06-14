import React, { Component } from "react";
import Form from "react-validation/build/form";
import { isEmail } from "validator";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import { withStyles } from "@material-ui/core/styles";
import AuthService from "../services/auth.service";
import Avatar from "@material-ui/core/Avatar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
<<<<<<< HEAD
import Input from "react-validation/build/input";
import CheckButton from "react-validation/build/button";
import { TextField } from "@material-ui/core";
=======
>>>>>>> e0c7edcf3990988a1fbf9d3da7cf9f013656fab2
import Grid from "@material-ui/core/Grid";
import { TextField } from "@material-ui/core";
import CheckButton from "react-validation/build/button";
import {Link} from 'react-router-dom';
<<<<<<< HEAD
// import { Input } from '@material-ui/core';
import './Login.css'


=======
import "./Login.css";
>>>>>>> e0c7edcf3990988a1fbf9d3da7cf9f013656fab2
const required = (value) => {
  if (!value) {
    return (
      <div className="alert alert-danger" role="alert">
        This field is required!
      </div>
    );
  }
};

const email = (value) => {
  if (!isEmail(value)) {
    return (
      <div className="alert alert-danger" role="alert">
        This is not a valid email.
      </div>
    );
  }
};
// style cho login
const useStyles = (theme) => ({
  // paper: {
  //   marginTop: theme.spacing(8),
  //   display: "block",
  //   flexDirection: "column",
  //   alignItems: "center",
  // },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  // form1: {
  //   width: "50%", // Fix IE 11 issue.
  //   marginTop: theme.spacing(1),
  //   display: "block",
  // },
  // submit: {
  //   margin: theme.spacing(3, 0, 2),
  // },
});

class Login extends Component {
  constructor(props) {
    super(props);
    this.handleLogin = this.handleLogin.bind(this);
    this.onChangeEmail = this.onChangeEmail.bind(this);
    this.onChangePassword = this.onChangePassword.bind(this);

    this.state = {
      email: "",
      password: "",
      loading: false,
      message: "",
    };
  }

  onChangeEmail(e) {
    this.setState({
      email: e.target.value,
    });
  }

  onChangePassword(e) {
    this.setState({
      password: e.target.value,
    });
  }

  handleLogin(e) {
    e.preventDefault();

    this.setState({
      message: "",
      loading: true,
    });

    this.form.validateAll();

    if (this.checkBtn.context._errors.length === 0) {
      AuthService.login(this.state.email, this.state.password).then(
        (res) => {
          if (res.jwt) {
            localStorage.setItem("loginstate", true);
            this.props.history.push("/");
            window.location.reload();
          }
        },
        (error) => {
          const resMessage =
            (error.response &&
              error.response.data &&
              error.response.data.message) ||
            error.message ||
            error.toString();

          this.setState({
            loading: false,
            message: resMessage,
          });
        }
      );
    } else {
      this.setState({
        loading: false,
      });
    }
  }

  render() {
    const { classes } = this.props;
    return (
      <div className="form">
        <div className="imageLogin">
          <Avatar className={classes.avatar}>
            <LockOutlinedIcon />
          </Avatar>
        </div>
        <div className="titleLogin">
          <Typography component="h1" variant="h5">
            Đăng nhập
          </Typography>
        </div>
        <form
          onSubmit={this.handleLogin}
          ref={(c) => {
            this.form = c;
          }}
        >
          <div className="loginForm">
            <input
              type="email"
              id="email"
              className="txtEmailControl"
              value={this.state.email}
              onChange={this.onChangeEmail}
              validations={[required, email]}
            />
          </div>
          <div className="loginForm">
            <input
              type="password"
              id="password"
              autoComplete="current-password"
              className="txtEmailControl"
              value={this.state.password}
              onChange={this.onChangePassword}
              validations={[required]}
            />
          </div>
          <div>
            <button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className="buttonSubmit"
              disabled={this.state.loading}
            >
              {this.state.loading && (
                <span className="spinner-border spinner-border-sm"></span>
              )}
              <span>Đăng nhập</span>
            </button>
            <Grid container justify="flex-end">
              <Grid item>
                {/* <Link href="#" variant="body2">
                    Already have an account? Sign in
                  </Link> */}
                <Link variant="body2" to={"/register"}>
                  Bạn chưa có tài khoản? Đăng kí ngay
                </Link>
              </Grid>
            </Grid>

            {this.state.message && (
              <div className="form-group">
                <div className="alert alert-danger" role="alert">
                  {this.state.message}
                </div>
              </div>
            )}

            {/* <CheckButton
              style={{ display: "none" }}
              ref={(c) => {
                this.checkBtn = c;
              }}
            /> */}
          </div>
        </form>
      </div>
    );
  }
}

export default withStyles(useStyles)(Login);
