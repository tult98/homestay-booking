import React, { Component } from "react";
import axios from "axios";
import { withStyles } from "@material-ui/core/styles";
import { CssBaseline } from "@material-ui/core";
import Grid from "@material-ui/core/Grid";
import Container from "@material-ui/core/Container";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import Header from "./Header";

import Button from "@material-ui/core/Button";
import { Slide } from "react-slideshow-image";
// import { Button} from 'react-bootstrap';


const useStyles = (theme) => ({
  sidebarAboutBox: {
    padding: theme.spacing(2),
    backgroundColor: theme.palette.grey[200],
  },
  sidebarSection: {
    marginTop: theme.spacing(3),
  },
  mainGrid: {
    marginTop: theme.spacing(3),
  },
  properties: {
    duration: 5000,
    transitionDuration: 500,
    infinite: true,
    indicators: true,
    arrows: true,
  },
  eachslide: {
    height: 700,
    
  },
});

class RoomDetail extends Component {
  state = {
    room: {},
    roomId: this.props.match.params.roomId,
    images: [],
  };

  componentDidMount() {
    axios
      .get("http://127.0.0.1:5000/api/accommodation/" + this.state.roomId)
      .then((response) => {
        this.setState({
          room: response.data,
          images: response.data.images,
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    const { classes } = this.props;
    const { room, images } = this.state;
    // console.log(images.map((image) => image.image_url));
    const imageArr = images.map((image) => image.image_url);
    return (
      <React.Fragment>
        <CssBaseline />
        <Header />
        <Container>
          <main>
            {/* noi dung post */}
            {/* Insert slideshow */}
            <Slide className={classes.properties}>
              <div
                className={classes.eachslide}
                style={{ backgroundImage: `url(${imageArr[1]})` }}
              ></div>
              <div
                className={classes.eachslide}
                style={{ backgroundImage: `url(${imageArr[2]})` }}
              ></div>
              <div
                className={classes.eachslide}
                style={{ backgroundImage: `url(${imageArr[3]})` }}
              ></div>
              <div
                className={classes.eachslide}
                style={{ backgroundImage: `url(${imageArr[4]})` }}
              ></div>
              <div
                className={classes.eachslide}
                style={{ backgroundImage: `url(${imageArr[5]})` }}
              ></div>
              <div
                className={classes.eachslide}
                style={{ backgroundImage: `url(${imageArr[6]})` }}
              ></div>
            </Slide>
            <Grid container spacing={5} className={classes.mainGrid}>
              <Grid item xs={12} md={8}>
                <h2>{room.name}</h2>
                <h3>{room.address}</h3>
                <p><b>Số phòng ngủ: {room.num_bedrooms}</b></p>
                <p><b>Số giường: {room.num_beds}</b></p>
                <p><b>Số phòng tắm: {room.num_bathrooms}</b></p>
                <code>{room.description}</code>
                <h3>Tiện nghi chỗ ở</h3>
                <h4>Loại giường:</h4>
                <h4>Tien ich bep</h4>
                <h3>Đánh giá</h3>
              </Grid>
              <div className="sidebar"></div>
              <Grid item xs={12} md={4}>
                <Paper elevation={0} className={classes.sidebarAboutBox}>
                  <Typography variant="h6" gutterBottom>
                    <h2>Giá tiền</h2>
                    <Button>Đặt ngay</Button>
                  </Typography>
                </Paper>
              </Grid>
            </Grid>
          </main>
        </Container>
      </React.Fragment>
    );
  }
}

export default withStyles(useStyles)(RoomDetail);
