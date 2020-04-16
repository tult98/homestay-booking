import React, {Component} from 'react';

class Header extends Component {
    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1>Homestay booking demo</h1>
                    <button id='btn-signup'>Sign up</button>
                    <button id='btn-login'>Log in</button>
                </header>
            </div>
            
        )
    }
}