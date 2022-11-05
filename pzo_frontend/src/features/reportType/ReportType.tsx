import React from 'react'

class ReportType extends React.Component {
    render(type:string) {
      return (
        <div className="page-title">
          type
        </div>
        
      );
    }
  }
  
export default React.memo(ReportType);