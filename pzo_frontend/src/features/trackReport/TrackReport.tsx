import React from 'react'
import Map from '../map/Map';

class ResponseReport extends React.Component {
    render(report) {
      return (
        <div className="track-report">
            <div className="report-type">
              <ReportType type={report.type} />
            </div>
            <div className="map">
              <Map />
            </div>
            <div className="report-info">
              <ReportInfo report={report} />
            </div>
            <div className="response-accepted">
              <ResponseReact report={report} />
            </div>
          
        </div>
        
      );
    }
  }
  
  // Przykład użycia: <ShoppingList name="Marek" />