import React from 'react';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Link from '@material-ui/core/Link';
import Pagination from "react-js-pagination"

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Homestay Booking Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const useStyles = makeStyles((theme) => ({
  icon: {
    marginRight: theme.spacing(2),
  },
  heroContent: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(8, 0, 6),
  },
  heroButtons: {
    marginTop: theme.spacing(4),
  },
  cardGrid: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(8),
  },
  card: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
  },
  cardMedia: {
    paddingTop: '56.25%', // 16:9
  },
  cardContent: {
    flexGrow: 1,
  },
  footer: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(6),
  },
  textcenter: {
    textAlign: "center",
  },
  pagination: {
    display: "inline-block",
    paddingLeft: 0,
    margin: '20px',
    borderRadius: '4px',

  },
}));

const cards = [1, 2, 3, 4, 5, 6, 7, 8, 9,  10, 11];

export default function Album() {
  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      <main>
        {/* Hero unit */}
        <div className={classes.heroContent}>
          <Container maxWidth="sm">
            <div className={classes.heroButtons}>
              <Grid container spacing={2} justify="center">
                <Grid item>
                  <Button variant="contained" color="primary">
                    Tìm nhanh
                  </Button>
                  <Button variant="contained" color="primary">
                    Tìm nhanh 2
                  </Button>
                  <Button variant="contained" color="primary">
                    Tìm nhanh 3
                  </Button>
                </Grid>
              </Grid>
            </div>
          </Container>
        </div>
        <Container className={classes.cardGrid} maxWidth="md">
          {/* End hero unit */}
          <Grid container spacing={4}>
            {cards.map((card) => (
              <Grid item key={card} xs={12} sm={6} md={4}>
                <Card className={classes.card}>
                  <CardMedia
                    className={classes.cardMedia}
                    image="https://source.unsplash.com/random"
                    title="Image title"
                  />
                    <CardContent className={classes.cardContent}>
                        <Typography>
                        Loại Homestay
                        </Typography>
                        <CardActions>
                            <Button gutterBottom variant="h4" component="h2" size='Medium'>
                                <b>
                                    Tên homestay
                                </b>
                            </Button>
                        </CardActions>
                        <Typography>
                            Kích thước: mấy người, mấy phòng...
                        </Typography>
                        <Typography>
                            <b>
                                Giá cả
                            </b>
                        </Typography>
                        <Typography>
                            Địa chỉ
                        </Typography>
                    </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid>
          <div className='textcenter'>
            <Pagination className='pagination'
            activePage={15}
            itemsCountPerPagee={10}
            totalItemsCount={20}
            pageRangeDisplayed={5}
            />
          </div>
          
          
        </Container>
        
      </main>
    </React.Fragment>
  );
}