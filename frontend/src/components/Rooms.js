import React, { Component } from "react";
import axios from "axios";
import { CardMedia } from "@material-ui/core";
import Button from "@material-ui/core/Button";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import "./Rooms.css";
import Pagination from "@material-ui/lab/Pagination";
import { Link } from "react-router-dom";
import Checkbox from "./CheckBox";

const itemsTypeRoom = ["Nguyên căn", "Phòng riêng", "Ở ghép"];

class Rooms extends Component {
  state = {
    posts: [],
    pagis: 0,
    page: 0,
    labelFilter: "",
    search: "",
    isShowTypeHomestayFrame: 0,
    isShowTypeBedFrame: 0,
    isShowTypeRoomFrame: 0,
    isShowNumBathRoomsFrame: 0,
    isShowNumBedRoomsFrame: 0,
    isShowNumBedsFrame: 0,
  };
  // Pagination
  componentDidMount() {
    axios
      .get("http://127.0.0.1:5000/api/accommodation/?size=30&page=1")
      .then((res) => {
        this.setState({
          posts: res.data.data,
          pagis: res.data.pagination.pages,
          page: 1,
        });
        console.log(res);
      });
  }
  // Cap nhat trang moi
  getNewPage = (numPage) => {
    axios
      .get("http://127.0.0.1:5000/api/accommodation/?size=30&page=" + numPage)
      .then((res) => {
        this.setState({
          posts: res.data.data,
        });
        console.log(res);
      });
  };

  // Filter 
  changeStateFilter1 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "property_type":"Chung cư"
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }
  changeStateFilter2 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "property_type": "Biệt Thự"
      })
      .then((response) => {
        console.log(response.data)
        this.setState({
          posts: response.data.data,
        });
      });
  }
  changeStateFilter3 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "property_type":"Căn hộ Studio"
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }
  changeStateFilter4 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "property_type":"Nhà riêng"
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }
  changeStateFilter5 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "property_type": "Căn hộ dịch vụ"
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }
  changeStateFilter6 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "property_type": "Khác"
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }
  changeStateFilter7 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "room_type": "Nguyên căn" 
      })
      .then((response) => {
        console.log(response.data)
        this.setState({
          
          posts: response.data.data,
        });
      });
      
  }
  changeStateFilter8 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "room_type": "Phòng riêng"
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }
  changeStateFilter9 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "room_type": "Ở ghép" 
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }
  changeStateFilter10 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "bed_type": "Futon" 
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }

  changeStateFilter11 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "bed_type": "Couch" 
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }

  changeStateFilter12 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "bed_type": "Real Bed" 
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }

  changeStateFilter13 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "bed_type": "Sofa Bed" 
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }
  changeStateFilter14 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "bed_type": "King size" 
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }
  changeStateFilter15 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "bed_type": "Queen Size" 
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }
  changeStateFilter16 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "bed_type": "Twins Bed" 
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }
  changeStateFilter17 = () => {
    axios
      .post("http://localhost:5000/api/accommodation/search", {
        "bed_type": "Bunk bed"
      })
      .then((response) => {
        this.setState({
          posts: response.data.data,
        });
      });
  }

  render() {
    const { posts, pagis, page} = this.state;
    if (posts.length)
      return (
        <div className="container">
          <React.Fragment>
            <main>
              <h3>Bộ lọc</h3>
              <ul>
              <li><div className="blockButtonFilter">
                <h4>Loại Homestay:</h4>
                <div className="filterButtonGroup">
                  <b>
                    <button
                      className="chckBoxFilter"
                      onClick={this.changeStateFilter1}
                    >
                      Căn hộ chung cư
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onClick={this.changeStateFilter2}
                    >
                      Biệt thự
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      id='Canhostudio'
                      onClick={this.changeStateFilter3}
                    >
                      Căn hộ Studio
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onClick={this.changeStateFilter4}
                    >
                      Nhà riêng
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onClick={this.changeStateFilter5}
                    >
                      Căn hộ dịch vụ
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onClick={this.changeStateFilter6}
                    >
                      Khác
                    </button>
                  </b>
                </div>
              </div>
              </li>
              <li><div className="blockButtonFilter">
                <h4>Loại phòng:</h4>
                <div className="filterButtonGroup">
                  <b>
                    <button
                      className="chckBoxFilter"
                      onClick={this.changeStateFilter7}
                    >
                      Nguyên căn
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onClick={this.changeStateFilter8}
                    >
                      Phòng riêng
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onClick={this.changeStateFilter9}
                    >
                      Ở ghép
                    </button>
                  </b>
                </div>
              </div>
              </li>
              <li>
              <div className="blockButtonFilter">
                <h4>Loại giường nằm:</h4>
                <div className="filterButtonGroup">
                  <b>
                    <button
                      className="chckBoxFilter"
                      onclick={this.changeStateFilter10}
                    >
                      Futon
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onclick={this.changeStateFilter11}
                    >
                      Couch
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onclick={this.changeStateFilter12}
                    >
                      Real Bed
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onclick={this.changeStateFilter13}
                    >
                      Sofa Bed
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onclick={this.changeStateFilter14}
                    >
                      King size
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onclick={this.changeStateFilter15}
                    >
                      Queen Size
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onclick={this.changeStateFilter16}
                    >
                      Twins Bed
                    </button>
                  </b>
                  <b>
                    <button
                      className="chckBoxFilter"
                      onclick={this.changeStateFilter17}
                    >
                      Bunk bed
                    </button>
                  </b>
                </div>
              </div>
              </li>
              </ul>
              {/* <div>
                <p>&emsp;</p>
              </div> */}
              <h2>
                <b>Những homestay nổi bật tại Trang homestay</b>
              </h2>
              <div>
                <p>&emsp;</p>
              </div>
              <Container maxWidth="lg">
                <Grid container spacing={4}>
                  {posts.map((post) => (
                    <Grid className="cardGrid" item xs={6} sm={6} md={4}>
                      <Card>
                        <CardMedia
                          className="cardMedia"
                          image={post.images[0].image_url}
                        />
                        <CardContent>
                          <Typography>
                            <b>
                              <i>Loại homestay: {post.property_type.name}</i>
                            </b>
                          </Typography>
                          <CardActions>
                            <Button
                              gutterbottom
                              variant="h1"
                              component="h1"
                              size="Medium"
                            >
                              <b>
                                <Link
                                  to={{
                                    pathname: `/rooms/${post.id}`,
                                  }}
                                >
                                  {post.name}
                                </Link>
                              </b>
                              <b>{post.price} VNĐ</b>
                            </Button>
                          </CardActions>
                        </CardContent>
                      </Card>
                    </Grid>
                  ))}
                </Grid>
              </Container>
            </main>
          </React.Fragment>
          <div>
            <p>&emsp;</p>
          </div>
          <div className="pagination">
            <Pagination
              count={pagis}
              page={page}
              defaultPage={this.state.page}
              onChange={this.handleChange}
            />
          </div>
        </div>
      );
    else return <div className="center">No posts yet</div>;
  }
}

export default Rooms;
