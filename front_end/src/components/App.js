import React from 'react';
import PageContainer from './PageContainer.js';

import pic from '../media/sand.jpg';

import styles from '../style/App.module.css'

export default class App extends React.Component {

  handler(){
    console.log("Clicked")
  }

  render() {
    return (
      <div className={styles.app}>

        {/* background image */}
        <img className={styles.art} src={pic} alt={"art"}></img>

        {/* headder */}
        <div className={styles.header}>
        </div>

        {/* body */}
        <div className={styles.body}>
          <PageContainer />
        </div>

        {/* footer */}
        <div className={styles.footer}>
        </div>
      </div>
    )
  }
}
