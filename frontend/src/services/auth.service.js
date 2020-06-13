import axios from 'axios'

const API_URL = 'http://192.168.199.31:5000/api/user/';

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
  
    register(email, first_name, last_name, phone_number, password1, password2) {
      return axios.post(API_URL + "register", {
        email,
        first_name,
        last_name, 
        phone_number, 
        password1, 
        password2
      });
    }
  
    getCurrentUser() {
      return JSON.parse(localStorage.getItem('user'));;
    }
  }
  
  export default new AuthService();