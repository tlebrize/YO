import React, { useEffect, useState } from 'react'
import { RouteComponentProps } from 'react-router'
import { getEpisodeData } from '../services/episodes'
import NavBar from '../components/NavBar'
import './EpisodePage.scss'


interface PlayerProps { url: string }

const Player = (props: PlayerProps) => {
  return (
    <iframe className='player' src={props.url} frameBorder="0" allow="autoplay; fullscreen; picture-in-picture" allowFullScreen></iframe>
  )
}

interface EpisodePageProps extends RouteComponentProps<{id: string}> {}

const EpisodePage = (props: EpisodePageProps) => {
  const [episode, setEpisode] = useState<Models.Episode | null>(null)

  useEffect(() => {
    getEpisodeData(props.match.params.id).then(data => {
      setEpisode(data)
    })
  }, [props.match.params.id])

  return (
    <>
      <NavBar />
      {!episode ? (
        <>
        </>
      ) : (
        <div className='episode'>
          <div className='episode__container'>
            <div className='blur'>
              <div className='title'>{episode.title}</div>
              <Player url={episode.url} />
            </div>
            <div className='buttonwrapper'>
              <button className='favorite'>
                <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fillRule="evenodd" clipRule="evenodd"><path d="M12 21.593c-5.63-5.539-11-10.297-11-14.402 0-3.791 3.068-5.191 5.281-5.191 1.312 0 4.151.501 5.719 4.457 1.59-3.968 4.464-4.447 5.726-4.447 2.54 0 5.274 1.621 5.274 5.181 0 4.069-5.136 8.625-11 14.402m5.726-20.583c-2.203 0-4.446 1.042-5.726 3.238-1.285-2.206-3.522-3.248-5.719-3.248-3.183 0-6.281 2.187-6.281 6.191 0 4.661 5.571 9.429 12 15.809 6.43-6.38 12-11.148 12-15.809 0-4.011-3.095-6.181-6.274-6.181"/></svg>
                <p>Ajouter aux favoris</p>
              </button>
              <button className='done'>
                <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fillRule="evenodd" clipRule="evenodd"><path d="M24 4.685l-16.327 17.315-7.673-9.054.761-.648 6.95 8.203 15.561-16.501.728.685z"/></svg>
                <p>Marquer comme fait</p>
              </button>
            </div>
            <div className='blur'>
              <div className='apropos'>À PROPOS</div>
              <p className='description'>{episode.description}</p>
            </div>
          </div>
        </div>
      )}
    </>
  )
}

export default EpisodePage
