import React, { Component } from 'react';
import "../../stylesheets/PlayItem.css";
import {PLAYITEM_STATUSES} from "../../constants";


class PlaylistDropdown extends Component {

    constructor(props) {
        super(props);

        this.state = {
            displayMenu: false
        };

        this.toggleDropdownMenu = this.toggleDropdownMenu.bind(this);

    };

    toggleDropdownMenu(event) {
        
        event.preventDefault();

        this.setState({
            displayMenu: !this.state.displayMenu 
        });

        console.log('toggleDropdownMenu:' + this.state.displayMenu )
    }

    render() {
        return (
            <div className="dropdown" >
                <div className="button" onClick={ this.toggleDropdownMenu }>
                    <button className="playitem-button">
                        <span className="playitem-button-icon"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"> <path d="M8 5h12v2H8zM7 19.5A3.5 3.5 0 1 0 3.5 16 3.5 3.5 0 0 0 7 19.5zm-2-4h1.5V14h1v1.5H9v1H7.5V18h-1v-1.5H5z"/> <circle cx="5" cy="10" r="1"/> <circle cx="5" cy="6" r="1"/> <path d="M8 9h12v2H8zm4 4h8v2h-8zm0 4h8v2h-8z"/> </svg></span>
                    </button>
                </div>


                { this.state.displayMenu ? (
                  <ul>

                      {

                          //(this.props.playlists === undefined || this.props.playlists.length == 0)
                              this.props.playlists.map(playlist => (

                          <li>
                              <a key={ playlist._id } onClick={ this.props.toogleItemPlaylist } >{playlist.name}</a>

                              { playlist.items === undefined || !playlist.items.includes(this.props.playitem._id) ? ('NOT_IN'):('IN')}
                          </li>
                           
                          
                      )) 
                      }

                     


                  </ul>
                  ) :
                  (
                  null
                  ) 
                }
            </div>

            );
    }
}

export default PlaylistDropdown;