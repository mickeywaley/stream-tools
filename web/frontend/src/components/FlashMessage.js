import React from 'react';

/**
 * @param  {[type]}
 * @param  {[type]}
 * @return {[type]}
 */
function foobar(x, y) {

}

export default function FlashMessage(props) {
    return (
        <div className="flash-error">
      {props.message}
    </div>
    );
}

FlashMessage.defaultProps = {
    message: 'An error occurred',
};