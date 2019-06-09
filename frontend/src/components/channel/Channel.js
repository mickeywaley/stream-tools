import React from 'react';

import {Link} from 'react-router-dom'


const Channel = props => {
    return (

        <div className="channel-item">
            <Link to={{pathname: "/channels/" + props.channel._id , state:{channel:props.channel} }} className="image"
               target="_self"
               title= { props.channel.name } >

                <img src="/images/loading.gif" data-echo={ props.channel.thumb } />

            </Link>

            <p className="title">
                { props.channel.name }
            </p>
        </div>


        );


};

export default Channel;
