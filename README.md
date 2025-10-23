# M0NARQ - Advanced Visualization Engines

M0NARQ is a showcase of two powerful data visualization engines: Hawkeye (visual analysis) and Hyperion (data analysis). This project demonstrates how complex data can be transformed into meaningful visual insights through advanced Python libraries and visualization techniques.

## Features

- **Hawkeye Engine**: Visual analysis engine for satellite imagery processing
  - Flood Analysis
  - Crop Monitoring
  - Urban Development
  - Night Light Analysis

- **Hyperion Engine**: Data analysis engine for pattern detection and insights
  - Freight Analysis
  - LPG Distribution
  - Predictive Modeling
  - Pattern Recognition

## Project Structure

```
mnq-website/
├── public/
│   ├── assets/
│   │   ├── demos/              # Demo preview images
│   │   ├── icons/              # Technology icons
│   │   └── processed/          # Processed satellite images
│   └── favicon.ico
├── src/
│   ├── styles/
│   │   └── main.css            # Main stylesheet
│   ├── scripts/
│   │   └── main.js             # Animation scripts
│   └── pages/
│       ├── index.html          # Homepage
│       ├── hawkeye.html        # Hawkeye engine page
│       └── hyperion.html       # Hyperion engine page
├── scripts/                    # Python scripts for image processing
│   └── process_image.py
└── .github/
    └── workflows/
        └── process_images.yml  # GitHub Actions workflow
```

## Deployment

This project is configured for easy deployment on Vercel:

1. Fork or clone this repository
2. Import into Vercel
3. Configure as a static site with:
   - Framework Preset: Static Site
   - Root Directory: `./`
   - Output Directory: `./src`

## Image Processing

Satellite imagery processing is handled through GitHub Actions:

1. Go to the Actions tab in this repository
2. Select "Process Satellite Images" workflow
3. Click "Run workflow"
4. Enter the satellite image URL and processing type
5. The processed image will be automatically added to the website

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Animations**: GSAP, Lenis for smooth scrolling
- **Image Processing**: Python, OpenCV, NumPy, Matplotlib
- **Deployment**: Vercel
- **CI/CD**: GitHub Actions

## License

MIT