import React from 'react'

function reportType(reportType:string) {
    return <h1>{reportType}</h1>;
}

export default React.memo(reportType);