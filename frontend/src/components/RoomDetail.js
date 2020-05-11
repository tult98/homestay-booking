import React, { Component } from "react";
import axios from "axios";
import { withStyles } from "@material-ui/core/styles";
import { CssBaseline } from "@material-ui/core";
import Grid from "@material-ui/core/Grid";
import Container from "@material-ui/core/Container";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import Header from './Header';

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
    console.log("This is data of room");
    console.log(room);
    return (
      <React.Fragment>
        <CssBaseline />
        <Header />
        <Container>
          <main>
            {/* noi dung post */}
            {/* <MainFeaturedPost post={mainFeaturedPost} />
            <Grid container spacing={4}>
              {featuredPosts.map((post) => (
                <FeaturedPost key={post.title} post={post} />
              ))}
            </Grid> */}
            
            <Grid container spacing={5} className={classes.mainGrid}>
              <Grid item xs={12} md={8}>
                <h2>{room.name}</h2>
                <p>{room.address}</p>
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
                    Khu vực hiển thị giá tiền và nút đặt phòng
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
