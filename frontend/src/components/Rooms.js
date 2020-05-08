import React, {Component} from 'react';
import axios from 'axios';
import { CardMedia } from '@material-ui/core';
import CssBaseline from '@material-ui/core/CssBaseline';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import './Rooms.css'
import Pagination from '@material-ui/lab/Pagination';
import { Link } from 'react-router-dom';

class Rooms extends Component {
  state = {
    posts: [ ],
    pagis: 0,
    page: 0
  }
  
  componentDidMount(){
    axios.get('http://localhost:5000/api/accommodation/?size=30&page=1')
    .then(res => {
      this.setState({
        posts: res.data.data,
        pagis: res.data.pagination.pages,
        page: 1
      })
    })
  }

  getNewPage = (numPage) => {
    axios.get('http://localhost:5000/api/accommodation/?size=30&page='+ numPage)
    .then(res => {
      this.setState({
        posts: res.data.data,
      })
    })
  }
  
  handleChange = (event, value) => {
    this.setState({
      page: value
    })
    this.getNewPage(value)
  };
  
  render() {
    const { posts, pagis, page } = this.state;
    if(posts.length)
      return (
        <div className="container">
          <React.Fragment>
              <CssBaseline />
              <main>
                <Container  maxWidth="lg">
                    <Grid container spacing={4}>
                      {posts.map((post) => (
                        <Grid className="cardGrid" item xs={6} sm={6} md={4}>
                          <Card>
                            <CardMedia
                              className="cardMedia"
                              image={post.images[0].image_url}
                              />
                              <CardContent className="room content">
                                <Typography>
                                  <b><i>Loại homestay: {post.property_type.name}</i></b>
                                </Typography>
                                <CardActions>
                                    <Button gutterbottom variant="h1" component="h1" size='Medium' >
                                        <b>
                                          <Link to={{
                                            pathname: `/rooms/${post.id}`
                                            }}>
                                            {post.name}
                                          </Link>
                                        </b>
                                    </Button>
                                </CardActions>
                                {/* <ul>
                                  <li>
                                    <Typography>
                                      Kích thước: {post.max_guess} người, {post.num_bathrooms} phòng tắm, {post.num_bedrooms} phòng ngủ
                                    </Typography>
                                  </li>
                                  <li>
                                    <Typography>
                                        {post.address}
                                    </Typography>
                                  </li>
                                </ul> */}
                                
                            </CardContent>
                          </Card>
                        </Grid>
                      ))}
                    </Grid>
                </Container>
              </main>
            </React.Fragment>
          <div className='pagination'>
            <Pagination count={pagis} page={page} defaultPage={this.state.page} onChange={this.handleChange}/>
          </div>
        </div>
      )
    else 
      return(
        <div className="center">No posts yet</div>
      )
  }
}

export default Rooms

