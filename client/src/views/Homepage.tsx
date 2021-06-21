import React, { useEffect, useState } from 'react'
import { getUserSeries } from '../services/series'
import './Homepage.scss'

const HomePage: React.FC = () => {

  const [series, setSeries] = useState<Models.Series | null>(null)

  // useEffect(() => {
  //   getUserSeries().then(data => {
  //     const seriesArray = data.map(
  //       (episodes: Array<Models.Episode>) => setSeries({
  //         title: episodes[0].series,
  //         episodes: episodes
  //       }))
  //     setSeries(seriesArray)
  //   })
  //   console.log(series)
  // })

  return (
    <div className='homepage'>Homepage</div>
  )
}
  
export default HomePage