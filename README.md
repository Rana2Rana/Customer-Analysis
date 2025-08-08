# Revenue Trends Across Digital Learning Formats

## Project Title
**Revenue Trends Across Digital Learning Formats**  
*An analysis of sales performance and customer behavior across digital educational products.*

---

## Dataset Overview
This dataset captures transactional data for digital educational products sold through various platforms and channels.  
It includes:

- **Product types**: Courses, eBooks, Coaching Programs, Templates, Webinars  
- **Customer info**: Gender, Country  
- **Sales info**: Quantity, Price, Revenue, Platform, Channel  
- **Time dimension**: Monthly sales with YTD and YoY comparison

---

## Business Goals
1. **Track revenue trends** over time and across product categories.  
2. **Evaluate marketing channel effectiveness** (Affiliate, Email, Facebook Ads).  
3. **Identify top-performing products** by sales and quantity.  
4. **Understand customer purchasing behavior** by gender and country.  
5. Highlight **YoY growth opportunities** and **potential sales drop risks**.

---

## Key Measures Created

| Measure Name            | Description                                          |
|-------------------------|------------------------------------------------------|
| `Total Sales`         | Sum of all revenue                                   |
| `Sales YTD`             | Year-to-date revenue                                 |
| `Sales YTD vs LY`       | YTD revenue from the previous year                   |
| `Sales YTD vs LY %`     | YoY growth percentage                                |
| `Total Quantity`        | Sum of units sold                                    |

---

## Visualizations & Insights

### 1. Revenue by Category (Pie Chart)
- Courses (19%) and Coaching Programs (17.9%) lead in revenue.
- Balanced distribution shows product diversity.

### 2. Monthly Sales Trend (Line Chart)
- Sales peaked in **March–April 2025**, with a decline starting May.
- July showed the lowest revenue — suggesting a need for mid-year re-engagement.

### 3. YTD Sales by Channel (Matrix Table)
- **Affiliate marketing** leads all channels in revenue and YoY growth.
- **Kajabi** and **ClickFunnels** outperform across all marketing strategies.
- All three marketing channels show **>110% YoY growth**.

### 4. Product Sales Behavior (Scatter Plot)
- Highlights relationship between quantity sold and total revenue.
- Top products (e.g., “Productivity Mastery”) show both high sales and volume.
- Useful for identifying pricing strategies and product bundling opportunities.

---

## Tools & Technologies Used
- **Power BI**: Data modeling, DAX calculations, report visuals  
- **DAX**: Custom measures for revenue comparison and time intelligence  
- **Python**: Initial data source preparation

---

## Learnings & Skills Demonstrated
- Time-based analysis using **YTD**, **YoY**, and **last year comparison**  
- **Dynamic visuals** for multi-dimensional data (category, time, channel)  
- Effective use of **scatter plots** to visualize revenue vs. quantity trends  
- **Data storytelling** through a clean, interactive dashboard

---

## Next Steps (Future Enhancements)
- Add drillthrough pages for detailed product-level insights  
- Include customer lifetime value (CLV) and retention tracking  
- Use slicers for gender, country, or product filtering for deeper segmentation
