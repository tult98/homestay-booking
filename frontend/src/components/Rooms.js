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

const itemsTypeHome = [
  "Căn hộ chung cư",
  "Biệt thự",
  "Căn hộ Studio",
  "Nhà riêng",
  "Căn hộ dịch vụ",
  "Khác",
];
const itemsTypeBedroom = [
  "Futon",
  "Couch",
  "Real Bed",
  "Sofa Bed",
  "King size",
  "Queen Size",
  "Twins Bed",
  "Bunk bed",
];
const itemsTypeRoom = ["Nguyên căn", "Phòng riêng", "Ở ghép"];

class Rooms extends Component {
  constructor(props) {
    super(props);
    this.onChangeSearch = this.onChangeSearch.bind(this);
    this.selectedCheckBoxSet = new Set();
  }

  state = {
    posts: [],
    pagis: 0,
    page: 0,
    search: "",
    isShowTypeHomestayFrame: 0,
    isShowTypeBedFrame: 0,
    isShowTypeRoomFrame: 0,
    isShowNumBathRoomsFrame: 0,
    isShowNumBedRoomsFrame: 0,
    isShowNumBedsFrame: 0,
  };
  onChangeSearch(e) {
    this.setState({
      search: e.target.value,
    });
  }
  componentDidMount() {
    axios
      .get("http://localhost:5000/api/accommodation/?size=30&page=1")
      .then((res) => {
        this.setState({
          posts: res.data.data,
          pagis: res.data.pagination.pages,
          page: 1,
        });
        console.log(res);
      });
  }
  getNewPage = (numPage) => {
    axios
      .get("http://localhost:5000/api/accommodation/?size=30&page=" + numPage)
      .then((res) => {
        this.setState({
          posts: res.data.data,
        });
        console.log(res);
      });
  };
  toggleCheckboxTypeHomestay = (label) => {
    // Co du lieu label
    // Tien hanh request theo label
    axios
      .post("/accommodation/search", {
        "property_type": { "name": label },
      })
      .then(function (response) {
        console.log(response);
        this.setState({
          posts: response.data.data,
        });
      })
      .catch(function (error) {
        console.log(error);
      });
  };
  toggleCheckboxTypeBed = (label) => {
    // Co du lieu label
    // Tien hanh request theo label
    document.getElementById('typeHomestayCheckbox').setState(({isChecked}) => ({
      isChecked: false,
    }));
    axios
      .post("/accommodation/search", {
        "bed_type": { "name": label },
      })
      .then(function (response) {
        console.log(response);
        this.setState({
          posts: response.data.data,
        });
      })
      .catch(function (error) {
        console.log(error);
      });
  };
  toggleCheckboxTypeRoom = (label) => {
    // Co du lieu label
    // Tien hanh request theo label
    axios
      .post("/accommodation/search", {
        "room_type": { "name": label },
      })
      .then(function (response) {
        console.log(response);
        this.setState({
          posts: response.data.data,
        });
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  createCheckboxTypeHomestay = (label) => (
    <b>
      <Checkbox
        className="chckBoxFilter"
        label={label}
        handleCheckboxChange={this.toggleCheckboxTypeHomestay}
        key={label}
        id='typeHomestayCheckbox'
      />
    </b>
  );
  createCheckboxTypeBed = (label) => (
    <b>
      <Checkbox
        className="chckBoxFilter"
        label={label}
        handleCheckboxChange={this.toggleCheckboxTypeBed}
        key={label}
      />
    </b>
  );
  createCheckboxTypeRoom = (label) => (
    <b>
      <Checkbox
        className="chckBoxFilter"
        label={label}
        handleCheckboxChange={this.toggleCheckboxTypeRoom}
        key={label}
      />
    </b>
  );

  // Create CheckBox when click button
  createCheckboxes = () => itemsTypeHome.map(this.createCheckboxTypeHomestay);
  createCheckboxesBedRoom = () =>
    itemsTypeBedroom.map(this.createCheckboxTypeBed);
  createCheckboxesTypeRoom = () =>
    itemsTypeRoom.map(this.createCheckboxTypeRoom);

  //---------------------------------------

  // Show CheckBox tuong ung voi nut bam
  // Loại homestay
  showTypeHomestayIframe = () => {
    const { isShowTypeHomestayFrame } = this.state;
    try {
      if (isShowTypeHomestayFrame === 0) {
        document.getElementById("typeHomeFrame").style.display = "flex";
        this.setState({
          isShowTypeHomestayFrame: 1,
          isShowTypeBedFrame: 0,
          isShowTypeRoomFrame: 0,
          isShowNumBedRoomsFrame: 0,
          isShowNumBedsFrame: 0,
          isShowNumBathRoomsFrame: 0,
        });
        document.getElementById("typeBedFrame").style.display = "none";
        document.getElementById("typeRoomsFrame").style.display = "none";
        document.getElementById("numBedRoomsFrame").style.display = "none";
        document.getElementById("numBedsFrame").style.display = "none";
        document.getElementById("numBathRooms").style.display = "none";
      } else {
        document.getElementById("typeHomeFrame").style.display = "none";
        this.setState({
          isShowTypeHomestayFrame: 0,
        });
      }
    } catch {}
  };
  // Loại giường ngủ
  showTypeBedIframe = () => {
    const { isShowTypeBedFrame } = this.state;
    try {
      if (isShowTypeBedFrame === 0) {
        document.getElementById("typeBedFrame").style.display = "flex";
        document.getElementById("typeRoomsFrame").style.display = "none";
        document.getElementById("numBedRoomsFrame").style.display = "none";
        document.getElementById("numBedsFrame").style.display = "none";
        document.getElementById("numBathRooms").style.display = "none";
        document.getElementById("typeHomeFrame").style.display = "none";
        this.setState({
          isShowTypeBedFrame: 1,
          isShowTypeHomestayFrame: 0,
          isShowTypeRoomFrame: 0,
          isShowNumBedRoomsFrame: 0,
          isShowNumBedsFrame: 0,
          isShowNumBathRoomsFrame: 0,
        });
      } else {
        document.getElementById("typeBedFrame").style.display = "none";
        this.setState({
          isShowTypeBedFrame: 0,
        });
      }
    } catch {}
  };
  // Loại phòng
  showTypeRoomIframe = () => {
    const { isShowTypeRoomFrame } = this.state;
    try {
      if (isShowTypeRoomFrame === 0) {
        document.getElementById("typeRoomsFrame").style.display = "flex";
        document.getElementById("typeBedFrame").style.display = "none";
        document.getElementById("numBedRoomsFrame").style.display = "none";
        document.getElementById("numBedsFrame").style.display = "none";
        document.getElementById("numBathRooms").style.display = "none";
        document.getElementById("typeHomeFrame").style.display = "none";
        this.setState({
          isShowTypeRoomFrame: 1,
          isShowTypeBedFrame: 0,
          isShowTypeHomestayFrame: 0,
          isShowNumBedRoomsFrame: 0,
          isShowNumBedsFrame: 0,
          isShowNumBathRoomsFrame: 0,
        });
      } else {
        document.getElementById("typeRoomsFrame").style.display = "none";
        this.setState({
          isShowTypeRoomFrame: 0,
        });
      }
    } catch {}
  };
  // Số phòng ngủ
  showNumBedRoomsIframe = () => {
    const { isShowNumBedRoomsFrame } = this.state;
    try {
      if (isShowNumBedRoomsFrame === 0) {
        document.getElementById("numBedRoomsFrame").style.display = "flex";
        document.getElementById("typeRoomsFrame").style.display = "none";
        document.getElementById("typeBedFrame").style.display = "none";
        document.getElementById("numBedsFrame").style.display = "none";
        document.getElementById("numBathRooms").style.display = "none";
        document.getElementById("typeHomeFrame").style.display = "none";
        this.setState({
          isShowNumBedRoomsFrame: 1,
          isShowTypeRoomFrame: 0,
          isShowTypeBedFrame: 0,
          isShowTypeHomestayFrame: 0,
          isShowNumBedsFrame: 0,
          isShowNumBathRoomsFrame: 0,
        });
      } else {
        document.getElementById("numBedRoomsFrame").style.display = "none";
        this.setState({
          isShowNumBedRoomsFrame: 0,
        });
      }
    } catch {}
  };
  // Số giường
  showNumBedsIframe = () => {
    const { isShowNumBedsFrame } = this.state;
    try {
      if (isShowNumBedsFrame === 0) {
        document.getElementById("numBedsFrame").style.display = "flex";
        document.getElementById("numBedRoomsFrame").style.display = "none";
        document.getElementById("typeRoomsFrame").style.display = "none";
        document.getElementById("typeBedFrame").style.display = "none";
        document.getElementById("numBathRooms").style.display = "none";
        document.getElementById("typeHomeFrame").style.display = "none";
        this.setState({
          isShowNumBedsFrame: 1,
          isShowNumBedRoomsFrame: 0,
          isShowTypeRoomFrame: 0,
          isShowTypeBedFrame: 0,
          isShowTypeHomestayFrame: 0,
          isShowNumBathRoomsFrame: 0,
        });
      } else {
        document.getElementById("numBedsFrame").style.display = "none";
        this.setState({
          isShowNumBedsFrame: 0,
        });
      }
    } catch {}
  };
  // Số phòng tắm
  showBathRoomsIframe = () => {
    const { isShowNumBathRoomsFrame } = this.state;
    try {
      if (isShowNumBathRoomsFrame === 0) {
        document.getElementById("numBathRooms").style.display = "flex";
        document.getElementById("numBedsFrame").style.display = "none";
        document.getElementById("numBedRoomsFrame").style.display = "none";
        document.getElementById("typeRoomsFrame").style.display = "none";
        document.getElementById("typeBedFrame").style.display = "none";
        document.getElementById("typeHomeFrame").style.display = "none";
        this.setState({
          isShowNumBathRoomsFrame: 1,
          isShowNumBedsFrame: 0,
          isShowNumBedRoomsFrame: 0,
          isShowTypeRoomFrame: 0,
          isShowTypeBedFrame: 0,
          isShowTypeHomestayFrame: 0,
        });
      } else {
        document.getElementById("numBathRooms").style.display = "none";
        this.setState({
          isShowNumBathRoomsFrame: 0,
        });
      }
    } catch {}
  };

  render() {
    const { posts, pagis, page } = this.state;
    if (posts.length)
      return (
        <div className="container">
          <React.Fragment>
            {/* <CssBaseline /> */}
            <main>
              <h3>
                <b>Tìm kiếm theo tiêu chí</b>
              </h3>
              <div className="btnGroup">
                {/* Button group filter */}
                <button
                  className="btnStyle"
                  onClick={this.showTypeHomestayIframe}
                >
                  Loại homestay
                </button>
                <button className="btnStyle" onClick={this.showTypeBedIframe}>
                  Loại giường ngủ
                </button>
                <button className="btnStyle" onClick={this.showTypeRoomIframe}>
                  Loại phòng
                </button>
                <button
                  className="btnStyle"
                  onClick={this.showNumBedRoomsIframe}
                >
                  Số phòng ngủ
                </button>
                <button className="btnStyle" onClick={this.showNumBedsIframe}>
                  Số giường
                </button>
                <button className="btnStyle" onClick={this.showBathRoomsIframe}>
                  Số phòng tắm
                </button>
              </div>
              <div className="checkBoxFrameALL">
                <Card id="typeHomeFrame" className="checkBoxFrame">
                  <form onSubmit={this.handleFormSubmit}>
                    {this.createCheckboxes()}
                    <div className="blockBtnFilter">
                      <button className="btnFilter" type="submit">
                        Filter
                      </button>
                    </div>
                  </form>
                </Card>
                <Card id="typeBedFrame" className="checkBoxFrame">
                  <form onSubmit={this.handleFormSubmit}>
                    {this.createCheckboxesBedRoom()}
                    <div className="blockBtnFilter">
                      <button className="btnFilter" type="submit">
                        Filter
                      </button>
                    </div>
                  </form>
                </Card>
                <Card id="typeRoomsFrame" className="checkBoxFrame">
                  <form onSubmit={this.handleTypeRoomFormSubmit}>
                    {this.createCheckboxesTypeRoom()}
                    <div className="blockBtnFilter">
                      <button className="btnFilter" type="submit">
                        Filter
                      </button>
                    </div>
                  </form>
                </Card>
                <Card id="numBedRoomsFrame" className="checkBoxFrame">
                  <form onSubmit={this.handleFormSubmit}>
                    <b>Nhập số phòng ngủ: </b>
                    <input type="text" className="inputNumBedRoom"></input>
                    <div className="blockBtnFilter">
                      <button className="btnFilter" type="submit">
                        Filter
                      </button>
                    </div>
                  </form>
                </Card>
                <Card id="numBedsFrame" className="checkBoxFrame">
                  <form onSubmit={this.handleFormSubmit}>
                    <b>Nhập số giường: </b>
                    <input type="text" className="inputNumBedRoom"></input>
                    <div className="blockBtnFilter">
                      <button className="btnFilter" type="submit">
                        Filter
                      </button>
                    </div>
                  </form>
                </Card>
                <Card id="numBathRooms" className="checkBoxFrame">
                  <form onSubmit={this.handleFormSubmit}>
                    <b>Nhập số phòng tắm: </b>
                    <input type="text" className="inputNumBedRoom"></input>
                    <div className="blockBtnFilter">
                      <button className="btnFilter" type="submit">
                        Filter
                      </button>
                    </div>
                  </form>
                </Card>
              </div>

              <div>
                <p>&emsp;</p>
              </div>
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
