import React from 'react';
import Channel from './Channel';

const ChannelList = props => {
    return (
        <div className="channel-list">

            { props.channels.map(channel => (
                  <Channel key={ channel._id } channel={ channel } />
              )) }
        </div>
        );
};

export default ChannelList;
