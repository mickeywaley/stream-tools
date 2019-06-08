import React, { Component } from 'react';
import { connect } from 'react-redux';

import PlayItemsPage from '../components/playitem/PlayItemsPage';
import FlashMessage from '../components/FlashMessage';

import Header from '../components/Header'
import Footer from '../components/Footer'

import Filters from '../components/filter/Filters';
import InputFilter from '../components/filter/InputFilter';

import { createPlayItem, editPlayItem, fetchPlayItems } from '../actions';

var allMovies = [
    {'title':'movie 1', 'year':'2016'},

    {'title':'movie 2', 'year':'2018'},
    {'title':'movie 3', 'year':'2018'},
    {'title':'movie 4', 'year':'2018'},

    {'title':'movie 5', 'year':'2018'},

    {'title':'movie 6', 'year':'2018'},
    {'title':'movie 7', 'year':'2019'},

]


class Home extends Component {

    state = {
        filters: { title: '' },
    }

    onFilterChange = (filters) => {
        console.log(filters)
        this.setState({ filters });
    }


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
        const { filters } = this.state;
        const movies = allMovies.filter(({ title }) => (
            title.includes(filters.title)
        ))

        return (

            <div>
                <Header />
                { this.props.error && <FlashMessage message={ this.props.error } /> }

                <Filters onChange={this.onFilterChange}>
                    <InputFilter filterName="title" />
                </Filters>
                <ul>
                    {movies.map(({ title }) => <li key={title}>{title}</li>)}
                </ul>


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