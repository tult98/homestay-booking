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
  "itemsTypeBedroom",
  "itemsTypeBedroom2",
  "itemsTypeBedroom3",
];
const itemsTypeRoom = ["itemsTypeRoom"];
const itemsNumBedrooms = ["itemsNumBedrooms"];
const itemsNumBeds = ["itemsNumBeds"];
const itemsNumBaths = ["itemsNumBaths"];
class Rooms extends Component {
  constructor(props) {
    super(props);
    this.onChangeSearch = this.onChangeSearch.bind(this);
  }
  state = {
    posts: [],
    pagis: 0,
    page: 0,
    search: "",
    isShow: 0,
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

  handleChange = (event, value) => {
    this.setState({
      page: value,
    });
    this.getNewPage(value);
  };

  handleChangeFilter = (value, arg1) => {
    axios
      .post("/accommodation/search", {
        arg1: value,
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

  componentWillMount = () => {
    this.selectedCheckboxes = new Set();
  };

  toggleCheckbox = (label) => {
    if (this.selectedCheckboxes.has(label)) {
      this.selectedCheckboxes.delete(label);
    } else {
      this.selectedCheckboxes.add(label);
    }
  };

  createCheckbox = (label) => (
    <b>
      <Checkbox
        className="chckBoxFilter"
        label={label}
        handleCheckboxChange={this.toggleCheckbox}
        key={label}
      />
    </b>
  );

  // Create CheckBox when click button
  createCheckboxes = () => itemsTypeHome.map(this.createCheckbox);
  createCheckboxesBedRoom = () => itemsTypeBedroom.map(this.createCheckbox);
  createCheckboxesTypeRoom = () => itemsTypeRoom.map(this.createCheckbox);
  createCheckboxesNumBedrooms = () => itemsNumBedrooms.map(this.createCheckbox);
  createCheckboxesNumBeds = () => itemsNumBeds.map(this.createCheckbox);
  createCheckboxesNumBaths = () => itemsNumBaths.map(this.createCheckbox);

  //---------------------------------------

  // Show CheckBox tuong ung voi nut bam
  showTypeHouseIframe = () => {
    const { isShow } = this.state;
    try {
      if (isShow === 1) {
        document.getElementById("typeHomeFrame").style.display = "none";
        this.setState({
          isShow: 0,
        });
      } else {
        document.getElementById("typeHomeFrame").style.display = "flex";
        this.setState({
          isShow: 1,
        });
      }
    } catch {}
  };
  showTypeBedRoomsIframe = () => {
    const { isShow } = this.state;
    try {
      if (isShow === 1) {
        document.getElementById("typeBedRoomsFrame").style.display = "none";
        this.setState({
          isShow: 0,
        });
      } else {
        document.getElementById("typeBedRoomsFrame").style.display = "flex";
        this.setState({
          isShow: 1,
        });
      }
    } catch {}
  };
  showTypeRoomIframe = () => {
    const { isShow } = this.state;
    try {
      if (isShow === 1) {
        document.getElementById("typeRoomsFrame").style.display = "none";
        this.setState({
          isShow: 0,
        });
      } else {
        document.getElementById("typeRoomsFrame").style.display = "flex";
        this.setState({
          isShow: 1,
        });
      }
    } catch {}
  };
  showNumBedRoomsIframe = () => {
    const { isShow } = this.state;
    try {
      if (isShow === 1) {
        document.getElementById("numBedRoomsFrame").style.display = "none";
        this.setState({
          isShow: 0,
        });
      } else {
        document.getElementById("numBedRoomsFrame").style.display = "flex";
        this.setState({
          isShow: 1,
        });
      }
    } catch {}
  };
  showNumBedsIframe = () => {
    const { isShow } = this.state;
    try {
      if (isShow === 1) {
        document.getElementById("numBedsFrame").style.display = "none";
        this.setState({
          isShow: 0,
        });
      } else {
        document.getElementById("numBedsFrame").style.display = "flex";
        this.setState({
          isShow: 1,
        });
      }
    } catch {}
  };
  showBathRoomsIframe = () => {
    const { isShow } = this.state;
    try {
      if (isShow === 1) {
        document.getElementById("numBathRooms").style.display = "none";
        this.setState({
          isShow: 0,
        });
      } else {
        document.getElementById("numBathRooms").style.display = "flex";
        this.setState({
          isShow: 1,
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
                <button className="btnStyle" onClick={this.showTypeHouseIframe}>
                  Loại homestay
                </button>
                <button
                  className="btnStyle"
                  onClick={this.showTypeBedRoomsIframe}
                >
                  Loại phòng ngủ
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
                      <button className="btnFilter" type="submit">
                        Cancel
                      </button>
                    </div>
                  </form>
                </Card>
                <Card id="typeBedRoomsFrame" className="checkBoxFrame">
                  <form onSubmit={this.handleFormSubmit}>
                    {this.createCheckboxesBedRoom()}
                    <div className="blockBtnFilter">
                      <button className="btnFilter" type="submit">
                        Filter
                      </button>
                      <button className="btnFilter" type="submit">
                        Cancel
                      </button>
                    </div>
                  </form>
                </Card>
                <Card id="typeRoomsFrame" className="checkBoxFrame">
                  <form onSubmit={this.handleFormSubmit}>
                    {this.createCheckboxesTypeRoom()}
                    <div className="blockBtnFilter">
                      <button className="btnFilter" type="submit">
                        Filter
                      </button>
                      <button className="btnFilter" type="submit">
                        Cancel
                      </button>
                    </div>
                  </form>
                </Card>
                <Card id="numBedRoomsFrame" className="checkBoxFrame">
                  <form onSubmit={this.handleFormSubmit}>
                    {this.createCheckboxesNumBedrooms()}
                    <div className="blockBtnFilter">
                      <button className="btnFilter" type="submit">
                        Filter
                      </button>
                      <button className="btnFilter" type="submit">
                        Cancel
                      </button>
                    </div>
                  </form>
                </Card>
                <Card id="numBedsFrame" className="checkBoxFrame">
                  <form onSubmit={this.handleFormSubmit}>
                    {this.createCheckboxesNumBeds()}
                    <div className="blockBtnFilter">
                      <button className="btnFilter" type="submit">
                        Filter
                      </button>
                      <button className="btnFilter" type="submit">
                        Cancel
                      </button>
                    </div>
                  </form>
                </Card>
                <Card id="numBathRooms" className="checkBoxFrame">
                  <form onSubmit={this.handleFormSubmit}>
                    <div>{this.createCheckboxesNumBaths()}</div>
                    <div className="blockBtnFilter">
                      <button className="btnFilter" type="submit">
                        Filter
                      </button>
                      <button className="btnFilter" type="submit">
                        Cancel
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
