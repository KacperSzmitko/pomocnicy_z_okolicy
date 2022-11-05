import React from 'react'

function ReportType(reportType:string) {
    return <h1>{reportType}</h1>;
}

export default React.memo(ReportType);