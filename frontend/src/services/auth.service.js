import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/api/user/';

class AuthService {
    login(email, password) {
      return axios
        .post(API_URL + "login", {
          email,
          password
        })
        .then(response => {
          if (response.data.jwt) {
            localStorage.setItem("user", JSON.stringify(response.data));
          }
  
          return response.data;
        });
    }
  
    logout() {
      localStorage.removeItem("user");
    }
  
    // register(email, email, password) {
    //   return axios.post(API_URL + "signup", {
    //     username,
    //     email,
    //     password
    //   });
    // }
  
    getCurrentUser() {
      return JSON.parse(localStorage.getItem('user'));;
    }
  }
  
  export default new AuthService();