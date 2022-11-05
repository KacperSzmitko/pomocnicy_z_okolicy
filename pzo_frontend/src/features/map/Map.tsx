import React, { useMemo } from "react";
import {
  GoogleMap,
  useJsApiLoader,
  MarkerF,
  CircleF,
} from "@react-google-maps/api";
import { useAppSelector } from "../../common/hooks";

const containerStyle = {
  width: "400px",
  height: "400px",
};

export interface PropType {
  lat: number;
  lng: number;
}

function Map({ lat, lng }: PropType) {
  const current_lat = useAppSelector(
    (state) => state.reducer.reportsSlice.current_latitude
  );
  const current_lng = useAppSelector(
    (state) => state.reducer.reportsSlice.current_altitude
  );
  const center = useMemo(
    () => ({ lat: current_lat, lng: current_lng }),
    [current_lat, current_lng]
  );
  const radius = useAppSelector(
    (state) => state.reducer.userInfoSlice.search_area
  );
  const { isLoaded } = useJsApiLoader({
    id: "google-map-script",
    googleMapsApiKey: "AIzaSyCOv6Fj9IET_ieFKC5hQ359MqZnGDrgBKg",
  });

  const [map, setMap] = React.useState(null);

  const onLoad = React.useCallback(
    function callback(map: any) {
      const bounds = new window.google.maps.LatLngBounds(center);
      map.fitBounds(bounds);
      setMap(map);
    },
    [center]
  );

  const onUnmount = React.useCallback(function callback(map: any) {
    setMap(null);
  }, []);

  return isLoaded ? (
    <GoogleMap
      mapContainerStyle={containerStyle}
      center={center}
      zoom={9}
      onLoad={onLoad}
      onUnmount={onUnmount}
    >
      <MarkerF
        position={center}
      />
      <MarkerF position={{ lat, lng }} />
      <CircleF center={center} radius={radius} />
    </GoogleMap>
  ) : (
    <></>
  );
}

export default React.memo(Map);
