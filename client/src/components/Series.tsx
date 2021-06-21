import React from 'react'
import './Series.scss'


interface EpisodeProps { data: Models.Episode }

const Episode = (props: EpisodeProps) => {
    return (
        <div>{props.data.title}</div>
    )
}

interface SeriesProps { title: string, episodes: Array<Models.Episode> }

const Series = (props: SeriesProps) => {
    return (
        <>
            <div className='title'>{props.title}</div>
            <div className='carrousel'>
                {props.episodes.map( episode => (<Episode data={episode} />))}
            </div>
        </>
    )
}

export default Series