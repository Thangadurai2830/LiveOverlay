# API Documentation

This document provides detailed information about the RTSP Livestream Viewer API endpoints, request/response formats, and authentication requirements.

## Base URL

```
http://localhost:5000/api
```

## Authentication

Currently, the API does not require authentication. However, it's recommended to implement authentication in a production environment.

## Endpoints

### Stream Management

#### Get Stream Status

Retrieves the current status of the RTSP stream.

```http
GET /stream/status
```

**Response**

```json
{
  "is_streaming": true,
  "url": "http://localhost:5000/static/streams/stream.m3u8"
}
```

#### Start Stream

Starts streaming from a provided RTSP URL.

```http
POST /stream/start
```

**Request Body**

```json
{
  "rtsp_url": "rtsp://example.com/stream"
}
```

**Response**

```json
{
  "status": "success",
  "message": "Stream started successfully",
  "url": "http://localhost:5000/static/streams/stream.m3u8"
}
```

#### Stop Stream

Stops the current stream.

```http
POST /stream/stop
```

**Response**

```json
{
  "status": "success",
  "message": "Stream stopped successfully"
}
```

### Overlay Management

#### List Overlays

Retrieves all saved overlays.

```http
GET /overlays
```

**Response**

```json
{
  "overlays": [
    {
      "id": "overlay_id",
      "type": "text",
      "content": "Sample Text",
      "position": {
        "x": 100,
        "y": 100
      },
      "size": {
        "width": 200,
        "height": 50
      },
      "color": "#ffffff",
      "fontSize": "24px"
    }
  ]
}
```

#### Create Overlay

Creates a new overlay.

```http
POST /overlays
```

**Request Body**

```json
{
  "type": "text",
  "content": "Sample Text",
  "position": {
    "x": 100,
    "y": 100
  },
  "size": {
    "width": 200,
    "height": 50
  },
  "color": "#ffffff",
  "fontSize": "24px"
}
```

**Response**

```json
{
  "status": "success",
  "message": "Overlay created successfully",
  "overlay": {
    "id": "overlay_id",
    "type": "text",
    "content": "Sample Text",
    "position": {
      "x": 100,
      "y": 100
    },
    "size": {
      "width": 200,
      "height": 50
    },
    "color": "#ffffff",
    "fontSize": "24px"
  }
}
```

#### Update Overlay

Updates an existing overlay.

```http
PUT /overlays/:id
```

**URL Parameters**

- `id`: The ID of the overlay to update

**Request Body**

```json
{
  "position": {
    "x": 150,
    "y": 150
  },
  "size": {
    "width": 300,
    "height": 75
  }
}
```

**Response**

```json
{
  "status": "success",
  "message": "Overlay updated successfully",
  "overlay": {
    "id": "overlay_id",
    "type": "text",
    "content": "Sample Text",
    "position": {
      "x": 150,
      "y": 150
    },
    "size": {
      "width": 300,
      "height": 75
    },
    "color": "#ffffff",
    "fontSize": "24px"
  }
}
```

#### Delete Overlay

Deletes an overlay.

```http
DELETE /overlays/:id
```

**URL Parameters**

- `id`: The ID of the overlay to delete

**Response**

```json
{
  "status": "success",
  "message": "Overlay deleted successfully"
}
```

## Error Responses

All endpoints return appropriate HTTP status codes and error messages in case of failure:

```json
{
  "status": "error",
  "message": "Error description"
}
```

Common error codes:

- `400`: Bad Request - Invalid input parameters
- `404`: Not Found - Resource not found
- `500`: Internal Server Error - Server-side error

## Rate Limiting

Currently, there are no rate limits implemented. Consider adding rate limiting for production use.

## CORS

Cross-Origin Resource Sharing (CORS) is enabled for development. Configure the allowed origins appropriately for production use.

## Development Notes

- For development purposes, ensure MongoDB is running locally on port 27017.
- FFmpeg must be installed and accessible in the system PATH.
- The streaming functionality requires sufficient disk space for temporary HLS files.
- Monitor memory usage when handling multiple concurrent streams.
