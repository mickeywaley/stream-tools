import React from 'react';


const Channel = props => {
    return (

        <div className="channel-item">
            <a className="image"
               target="_blank"
               title= { props.channel.name } ><img src="./images/loading.gif" data-echo={ props.channel.thumb } /></a>
            <p className="title">
                { props.channel.name }
            </p>
        </div>


        );


};

export default Channel;
