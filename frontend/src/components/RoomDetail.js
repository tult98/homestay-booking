import React, { Component } from "react";
import axios from "axios";

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
    const { room, roomId } = this.state;
    console.log("This is data of room");
    console.log(room);
    return (
      <div className="container">
        <div className="wrapper">{/* slide show image of rooms */}</div>
        <div className="detail">
          <div className="row">
            <div className="detail-left">
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
            </div>
            <div className="sidebar"></div>
          </div>
        </div>
      </div>
    );
  }
}

export default RoomDetail;
