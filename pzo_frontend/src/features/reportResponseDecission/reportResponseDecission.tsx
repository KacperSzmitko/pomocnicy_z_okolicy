import React from 'react'

function ReportResponseDecission() {
    //TODO logika do przycisków 

    return  <div>
                <button className="deny-button">DENY</button> 
                <button className="accept-button">ACCEPTED</button>
            </div>;
}

export default React.memo(ReportResponseDecission);