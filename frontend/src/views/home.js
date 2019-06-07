import React, { Component } from 'react';
import { connect } from 'react-redux';
import PlayItemsPage from '../components/PlayItemsPage';
import FlashMessage from '../components/FlashMessage';
import { createPlayItem, editPlayItem, fetchPlayItems } from '../actions';

import Header from '../containers/Header'
import Footer from '../containers/Footer'

class Home extends Component {
    componentDidMount() {
        this.props.dispatch(fetchPlayItems());
    }

    onCreatePlayItem = ({title, description}) => {
        this.props.dispatch(createPlayItem({
            title,
            description
        }));
    };

    onStatusChange = (id, status) => {
        this.props.dispatch(editPlayItem(id, {
            status
        }));
    };

    render() {
        return (

            <div>
                <Header />
                { this.props.error && <FlashMessage message={ this.props.error } /> }
                <div className="main-content">
                    <PlayItemsPage playitems={ this.props.playitems }
                        onCreatePlayItem={ this.onCreatePlayItem }
                        onStatusChange={ this.onStatusChange }
                        isLoading={ this.props.isLoading } />
                </div>
                <Footer />
            </div>
            );
    }
}

function mapStateToProps(state) {
    const {playitems, isLoading, error} = state.playitems;
    return {
        playitems,
        isLoading,
        error
    };
}

export default connect(mapStateToProps)(Home);