import React from 'react'

function reportResponseDecission() {
    //TODO logika do przycisków 

    return  <div>
                <button className="deny-button">DENY</button> 
                <button className="accept-button">ACCEPTED</button>
            </div>;
}

export default React.memo(reportResponseDecission);