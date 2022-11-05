import React from 'react'
import Map from '../map/Map';
import ReportType from '../reportType/ReportType'

class ResponseReport extends React.Component {
    render(report) {
      return (
        <div className="response-report">
            <div className="report-type">
                <ReportType type={report.type} />
            </div>
            <div className="map">
                <Map />
            </div>
            <div className="report-info">
                <ReportInfo report={report} />
            </div>
            <div className="response-react">
                <ResponseReact report={report} />
            </div>
        </div>
      );
    }
  }
  
  // Przykład użycia: <ShoppingList name="Marek" />