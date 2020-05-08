import React, {Component} from 'react';
import axios from 'axios';


class RoomDetail extends Component{

    state = {
        room: {}, 
        roomId: this.props.match.params.roomId
    }

    componentDidMount () {
        axios.get('http://127.0.0.1:5000/api/accommodation/' + this.state.roomId)
        .then(response => {
            this.setState({
                room: response.data
            });
        }).catch(error => {
            console.log(error)
        })
    }

    render () {
        const {room, roomId} = this.state;
        console.log("This is data of room");
        console.log(room)
        return <div>Hello </div>
    }
}

export default RoomDetail;