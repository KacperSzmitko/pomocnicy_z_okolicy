import React from 'react'

function ReportTrackDecission(reportType:string) {
    //TODO logika do przycisku

    return  <div>
                <button className="small-deny-button">DENY</button> 
                <div className="accepted-button-residue">ACCEPTED</div>
            </div>;
}

export default React.memo(ReportTrackDecission);