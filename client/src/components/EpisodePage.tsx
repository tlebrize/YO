import React from 'react'
import { RouteComponentProps } from 'react-router'

interface EpisodePageProps extends RouteComponentProps<{uuid: string}> {}

const EpisodePage: React.FC<EpisodePageProps> = (props) => (
  <div>EpisodePage {props.match.params.uuid}</div>
)

export default EpisodePage
