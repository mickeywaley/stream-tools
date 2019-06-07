import React from 'react';

import { PLAYITEM_STATUSES } from '../constants';

const PlayItem = props => {
    return (
        <div className="playitem">
            <div className="playitem-header">
                <div>
                    { props.playitem.name }
                </div>
                <select value={ props.playitem.status } onChange={ onStatusChange }>
                    { PLAYITEM_STATUSES.map(status => (
                          <option key={ status } value={ status }>
                              { status }
                          </option>
                      )) }
                </select>
            </div>
            <hr />
            <div className="playitem-body">
                { props.playitem.url }
            </div>
        </div>
        );

    function onStatusChange(e) {
        props.onStatusChange(props.playitem.id, e.target.value);
    }
};

export default PlayItem;
