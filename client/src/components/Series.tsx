import { useHorizontalScroll } from '../lib/hooks/horizontalScroll'
import React from 'react'
import { Link } from 'react-router-dom'
import './Series.scss'

interface EpisodeProps { data: Models.Episode }

const Episode = (props: EpisodeProps) => {
  return (
    <div className='episode-preview'>
      <Link to={`/episode/${props.data.id}`}>
        <img className='episode-preview__thumbnail' src={props.data.thumbnail} />
        <div className='episode-preview__title'>{props.data.title}</div>
      </Link>
    </div>
  )
}

interface SeriesProps { title: string, episodes: Array<Models.Episode> }

const Series = (props: SeriesProps) => {
  
  const [ref, scroll, scrollTo] = useHorizontalScroll();

  return (
    <div className='series'>
      <div className='series__title'>{props.title}</div>
      { scroll && scroll.position !== 0 && (
        <button className='series__button-left' onClick={() => scrollTo(scroll, 'left', 1350)}>
          <svg width="24" height="24" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"/></svg>
        </button>
      )}
      <div className='carrousel' ref={ref}>
        {props.episodes.map( episode => (<div key={episode.id}><Episode data={episode} /></div>))}
      </div>
      {scroll && scroll.position !== scroll.width && <button className='series__button-right' onClick={() => scrollTo(scroll, 'right', 1350)}><svg width="24" height="24" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"/></svg></button> }
    </div>
  )
}

export default Series