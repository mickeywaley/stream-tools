import React from 'react';
import PlayItem from './PlayItem';

const PlayItemList = props => {
    return (
        <div className="playitem-list">
            <div className="playitem-list-title">
                <strong>{ props.status }</strong>
            </div>
            { props.playitems.map(playitem => (
                  <PlayItem key={ playitem._id } playitem={ playitem } playlists={ props.playlists } onStatusChange={ props.onStatusChange } />
              )) }
        </div>
        );
};

export default PlayItemList;
