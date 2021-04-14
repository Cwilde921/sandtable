import React from 'react'

export default class ColorCenter extends React.Component {
    render(){
        return (
            <div>
                <h2>Color Center</h2>
                <button onClick={ () => this.props.handler(0) }>home</button>
                <br />
                <label htmlFor={"color_select"} />
                <input id={"color_select"} name={"color"} type={'color'} onChange={ () => console.log( document.getElementById("color_select").value ) } />
            </div>
        )
    }
}