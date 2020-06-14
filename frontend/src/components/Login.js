import React, { Component } from "react";
import Form from "react-validation/build/form";
import { isEmail } from "validator";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import { withStyles } from "@material-ui/core/styles";
import AuthService from "../services/auth.service";
import Avatar from "@material-ui/core/Avatar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import Input from "react-validation/build/input";
import CheckButton from "react-validation/build/button";
import { TextField } from "@material-ui/core";
import Grid from "@material-ui/core/Grid";
import {Link} from 'react-router-dom';
// import { Input } from '@material-ui/core';
import './Login.css'


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
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form1: {
    width: "50%", // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
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
      <div className="col-md-12">
        <div className={classes.paper}>
          <Avatar className={classes.avatar}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Đăng nhập
          </Typography>
          <Form
            className={classes.form1}
            noValidate
            onSubmit={this.handleLogin}
            ref={(c) => {
              this.form = c;
            }}
          >
            <input
              
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              autoComplete="email"
              autoFocus
              type="email"
              className="form-control"
              value={this.state.email}
              onChange={this.onChangeEmail}
              validations={[required, email]}
            />

            <input
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
              className="form-control"
              value={this.state.password}
              onChange={this.onChangePassword}
              validations={[required]}
            />

            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
              disabled={this.state.loading}
            >
              {this.state.loading && (
                <span className="spinner-border spinner-border-sm"></span>
              )}
              <span>Đăng nhập</span>
            </Button>

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
           
            <CheckButton
              style={{ display: "none" }}
              ref={(c) => {
                this.checkBtn = c;
              }}
            />
          </Form>
        </div>
      </div>
    );
  }
}

export default withStyles(useStyles)(Login);
