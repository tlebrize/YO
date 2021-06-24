import React, { useEffect, useState } from 'react'
import { getUserSeries } from '../services/series'
import Series from '../components/Series'
import NavBar from '../components/NavBar'
import './Homepage.scss'

const HomePage: React.FC = () => {

  const [series, setSeries] = useState<Array<Models.Series> | null>(null)

  useEffect(() => {
    getUserSeries().then(data => {
      const seriesArray = data.map(
        (episodes: Array<Models.Episode>) => 
        ({
          title: episodes[0].series,
          episodes: episodes
        })
      )
      setSeries(seriesArray)
    })
  }, [])

  return (
    <>
      <NavBar />
      {!series ? (
        <>
        </>
      ) : (
        <div className='series-container'>
          {series.map(
            s => (<div key={s.title}><Series title={s.title} episodes={s.episodes}/></div>)
          )}
        </div>
      )}
    </>
  )
}
  
export default HomePage