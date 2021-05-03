import React from 'react'

import styles from '../../style/PatternManager.module.css'

export default class PatternManager extends React.Component {
    constructor(params){
        super(params)
        this.res = {
            file: null,
        }
    }

    send_file() {
        fetch("localhost:5000/api",{
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({'hello': "world"})
        })//.then((res) => res.json())
        .then((res) => console.log(res))
    }

    render(){
        return (
            <div className={styles.body}>
                <h1>Pattern Manager</h1>
                <p>Make patterns with sandify and upload them here in thr format.</p>
                <form onSubmit={() => {this.send_file()}} >
                    <label id={"pattern_file_label"} htmlFor={"pattern_file"} className={styles.inpt} > Upload Pattern </label>
                    <input id={"pattern_file"} className={styles.inpt} type={"file"} onChange={(event)=>{
                        this.res.file = event.target.files.item(0)
                        document.getElementById("pattern_file_label").innerHTML = this.res.file.name
                    }} />
                    <br/>
                    <input type={"submit"} className={styles.inpt} value={"Submit Pattern"} />
                </form>
                <hr/>
                <button className={styles.inpt} onClick={ () => this.props.handler(0) }>Home</button>
                <button className={styles.inpt} onClick={ () => window.location.href="https://sandify.org" } >Go To Sandify</button>
            </div>
        )
    }
}