import React, { Component } from "react";
import axios from "axios";
import { withStyles } from "@material-ui/core/styles";
import { CssBaseline } from "@material-ui/core";
import Grid from "@material-ui/core/Grid";
import Container from "@material-ui/core/Container";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import Header from "./Header";
import { Slide } from "react-slideshow-image";

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
});

class RoomDetail extends Component {
  state = {
    room: {},
    roomId: this.props.match.params.roomId,
  };

  componentDidMount() {
    axios
      .get("http://127.0.0.1:5000/api/accommodation/" + this.state.roomId)
      .then((response) => {
        this.setState({
          room: response.data,
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    const { classes } = this.props;
    const { room } = this.state;
    console.log(room);
    const properties = {
      duration: 5000,
      transitionDuration: 500,
      infinite: true,
      indicators: true,
      arrows: true,
    };
    return (
      <React.Fragment>
        <CssBaseline />
        <Header />
        <Container>
          <main>
            {/* noi dung post */}
            {/* Insert slideshow */}
            <Slide {...properties}>
              <div className="each-slide">
                <div style={{ backgroundImage: `url(${room.image[0]})` }}>
                  {/* <span>Slide 1</span> */}
                </div>
              </div>
              <div className="each-slide">
                <div style={{ backgroundImage: `url(${room.image[1]})` }}>
                  {/* <span>Slide 2</span> */}
                </div>
              </div>
              <div className="each-slide">
                <div style={{ backgroundImage: `url(${room.image[2]})` }}>
                  {/* <span>Slide 3</span> */}
                </div>
              </div>
              <div className="each-slide">
                <div style={{ backgroundImage: `url(${room.image[3]})` }}>
                  {/* <span>Slide 3</span> */}
                </div>
              </div>
              <div className="each-slide">
                <div style={{ backgroundImage: `url(${room.image[4]})` }}>
                  {/* <span>Slide 3</span> */}
                </div>
              </div>
            </Slide>
            <Grid container spacing={5} className={classes.mainGrid}>
              <Grid item xs={12} md={8}>
                <h2>{room.name}</h2>
                <h3>{room.address}</h3>
                <p> dien tich</p>
                <p> kich thuoc </p>
                <p>{room.description}</p>
                <h3> Tien nghi cho o</h3>
                <h4> tien ich</h4>
                <h4>Tien ich bep</h4>
                <h3> gia phong</h3>
                <h3> danh gia</h3>
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
