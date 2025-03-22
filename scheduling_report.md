# Crestwood College Scheduling Report

## Introduction

This report presents the results of the scheduling process for Crestwood College using operational research techniques. The scheduling algorithm was designed to optimize course assignments based on student preferences while respecting various constraints.

## Operational Research Approach

The scheduling problem was approached as a combination of two classic operations research problems:

1. **Assignment Problem**: Matching students to course sections
2. **Transportation Problem**: Distributing course sections across time blocks

### Key Concepts Used

- **Hungarian Algorithm**: A combinatorial optimization algorithm that solves the assignment problem in polynomial time
- **Cost Matrix**: A mathematical representation of the preferences and constraints where lower values indicate better assignments
- **Multi-objective Optimization**: Balancing multiple goals including student preferences, room capacity, and teacher availability

### Implementation Strategy

The implementation followed a phased approach:

1. **Priority-Based Assignment**: First assigning required courses, then requested, and finally recommended
2. **Constraint Handling**: Ensuring no student or teacher is double-booked and respecting room capacities
3. **Optimization Refinement**: Using hill-climbing techniques to improve the initial schedule

## Overall Statistics

Total requests: 1259
Total fulfilled: 1030 (81.81%)
Total unfulfilled: 229 (18.19%)

## Priority Breakdown

| Priority | Fulfilled | Unfulfilled | Total | Fulfillment Rate |
|----------|-----------|-------------|-------|------------------|
| **Required** | 178 | 0 | 178 | 100.00% |
| **Requested** | 811 | 152 | 963 | 84.22% |
| **Recommended** | 41 | 77 | 118 | 34.75% |

## Resolved & Unresolved Requests Statistics

### Overall Resolution Status

| Resolution | Count | Percentage |
|------------|-------|------------|
| **Resolved** | 1030 | 81.81% |
| **Unresolved** | 229 | 18.19% |
| **Total** | 1259 | 100.00% |


### Priority-wise Resolution Statistics

| Priority | Resolved | Unresolved | Total | Resolution Rate |
|----------|----------|------------|-------|----------------|
| **Required** | 178 | 0 | 178 | 100.00% |
| **Requested** | 811 | 152 | 963 | 84.22% |
| **Recommended** | 41 | 77 | 118 | 34.75% |

## Course Popularity Analysis

### Most Popular Courses

| Course | Students Enrolled | % of Total Students |
|--------|-------------------|---------------------|
| Spanish II | 44 | 28.21% |
| Bible 11 | 41 | 26.28% |
| Bible 10 | 40 | 25.64% |
| Bible 12 | 37 | 23.72% |
| US History | 33 | 21.15% |
| Bible 9 | 30 | 19.23% |
| Chemistry Honors | 30 | 19.23% |
| American Government & Politics | 29 | 18.59% |
| Health - High  | 29 | 18.59% |
| Digital Imaging & Editing | 28 | 17.95% |

## Block Utilization Analysis

### Student Distribution Across Blocks

| Block | Number of Students | Utilization % |
|-------|-------------------|---------------|
| 1A | 144 | 92.31% |
| 1B | 146 | 93.59% |
| 2A | 146 | 93.59% |
| 2B | 146 | 93.59% |
| 3 | 148 | 94.87% |
| 4A | 152 | 97.44% |
| 4B | 148 | 94.87% |

## Student Satisfaction Metrics

### Overall Student Scheduling Completeness

| Satisfaction Level | Count | Percentage |
|---------------------|-------|------------|
| **Full Schedule** (All blocks) | 139 | 89.10% |
| **Partial Schedule** (Some blocks) | 17 | 10.90% |
| **Required Courses Fulfilled** | 156 | 100.00% |


## Students Block-wise View

This view shows all students assigned to each block.

### Block 1A

| Student ID | Course |
|------------|--------|
| 5361789 | Advanced Robotics |
| 5361796 | Algebra 1 |
| 5361797 | US History |
| 5361798 | Health - High  |
| 5361799 | US History |
| 5361801 | Health - High  |
| 5361802 | Spanish I |
| 5361803 | Digital Imaging & Editing |
| 5361804 | US History |
| 5361805 | Geometry Honors |
| 5361806 | Algebra 1 Honors |
| 5361807 | US History |
| 5361808 | Spanish I |
| 5361810 | Algebra 1 Honors |
| 5361813 | Bible 9 |
| 5361814 | Algebra 1 |
| 5361816 | Biology Honors |
| 5361817 | English 9 |
| 5361818 | Bible 9 |
| 5361819 | Biology |
| 5361820 | English 9 |
| 5361822 | English 9 Honors |
| 5361825 | Bible 9 |
| 5361827 | Algebra II |
| 5361828 | Graphic Design |
| 5361830 | Alg II Honors |
| 5361831 | Geometry |
| 5361832 | Bible 10 |
| 5361833 | Bible 10 |
| 5361834 | American Government & Politics |
| 5361835 | Geometry |
| 5361836 | Digital Imaging & Editing |
| 5361838 | Bible 10 |
| 5361840 | Advanced Robotics |
| 5361842 | Spanish II |
| 5361843 | Chemistry Honors |
| 5361844 | English 10 Honors |
| 5361845 | American Government & Politics Honors |
| 5361846 | Chemistry Honors |
| 5361847 | Bible 10 |
| 5361851 | Algebra II |
| 5361853 | Studio Art I |
| 5361856 | Spanish II |
| 5361857 | English 10 Honors |
| 5361858 | Bible 10 |
| 5361859 | American Government & Politics Honors |
| 5361862 | English 10 Honors |
| 5361863 | Bible 10 |
| 5361864 | Bible 10 |
| 5361865 | Bible 10 |
| 5361867 | Bible 10 |
| 5361868 | Spanish II |
| 5361869 | Spanish II |
| 5361870 | Spanish II |
| 5361871 | English 10 |
| 5361872 | Chemistry Honors |
| 5361873 | American Literature Honors |
| 5361874 | Bible 11 |
| 5361877 | Study Hall |
| 5361878 | World History |
| 5361879 | Band - High  |
| 5361880 | Bible 11 |
| 5361881 | Band - High  |
| 5361882 | Bible 11 |
| 5361883 | Studio Art II |
| 5361884 | Broadcast Journalism |
| 5361885 | Geometry Honors |
| 5361886 | Marine Biology |
| 5361887 | Band - High  |
| 5361888 | American Literature |
| 5361889 | Financial Literacy |
| 5361890 | Algebra II |
| 5361891 | Trig/Algebra III |
| 5361892 | World History |
| 5361893 | Physical Science |
| 5361895 | Health - High  |
| 5361896 | Algebra II |
| 5361897 | Bible 11 |
| 5361898 | American Literature |
| 5361899 | American Literature |
| 5361900 | Trig/PreCalculus |
| 5361901 | World History |
| 5361902 | American Literature |
| 5361903 | American Literature Honors |
| 5361904 | Bible 11 |
| 5361905 | World History |
| 5361906 | Dual Enrollment World Civ. 101 |
| 5361907 | Bible 12 |
| 5361908 | Personal Fitness |
| 5361909 | Trig/Algebra III |
| 5361910 | Dual Enrollment English 151 |
| 5361911 | Dual Enrollment World Civ. 101 |
| 5361912 | World Literature |
| 5361913 | Personal Fitness |
| 5361914 | Study Hall |
| 5361915 | Digital Imaging & Editing |
| 5361917 | Dual Enrollment Biology 101 |
| 5361919 | Study Hall |
| 5361920 | Trig/PreCalculus |
| 5361921 | AP Computer Science |
| 5361922 | Bible 12 |
| 5361923 | AP Calculus A/B |
| 5361924 | Bible 12 |
| 5361925 | Trig/PreCalculus |
| 5361926 | Yearbook |
| 5361927 | Dual Enrollment English 151 |
| 5361928 | Statistics Honors |
| 5361930 | Graphic Design |
| 5361932 | Bible 12 |
| 5361933 | Executive Internship I |
| 5361935 | Executive Internship I |
| 5361936 | Executive Internship I |
| 5361937 | AP Calculus A/B |
| 5407480 | American Literature Honors |
| 5407481 | Bible 9 |
| 5407488 | American Government & Politics |
| 5407494 | Spanish II |
| 5407497 | Health - High  |
| 5407498 | Executive Internship II |
| 5407499 | American Literature Honors |
| 5407500 | Chemistry Honors |
| 5407506 | Executive Internship I |
| 5407517 | Band - High  |
| 5407518 | English 10 |
| 5407519 | English 10 |
| 5407520 | Digital Imaging & Editing |
| 5407527 | Study Hall (Semester) |
| 5407543 | Algebra II |
| 5407554 | Geometry |
| 5407556 | American Literature Honors |
| 5407560 | English 10 |
| 5407561 | Trig/PreCalculus |
| 5407564 | Trig/Pre-Calculus Hon |
| 5407584 | English 9 |
| 5407593 | American Literature Honors |
| 5409913 | Bible 11 |
| 5424569 | Biology |
| 5424570 | Spanish I |
| 5432621 | World History |
| 5434946 | Drawing and Painting |
| 5439293 | Health - High  |
| 5510555 | US History |
| 5593175 | Executive Internship I |
| 5642283 | English 9 |

### Block 1B

| Student ID | Course |
|------------|--------|
| 5361789 | Physics Honors |
| 5361796 | US History |
| 5361797 | Geometry Honors |
| 5361798 | Geometry Honors |
| 5361799 | English 9 |
| 5361800 | Biology |
| 5361801 | Biology |
| 5361802 | English 9 Honors |
| 5361803 | Bible 9 |
| 5361804 | Spanish I |
| 5361806 | Spanish I |
| 5361807 | Algebra 1 Honors |
| 5361808 | Bible 9 |
| 5361809 | US History |
| 5361810 | Biology |
| 5361813 | English 9 |
| 5361814 | Health - High  |
| 5361816 | Health - High  |
| 5361817 | US History |
| 5361818 | Spanish I |
| 5361819 | Health - High  |
| 5361820 | Physical Education - High  |
| 5361822 | Bible 9 |
| 5361825 | Biology Honors |
| 5361827 | Drawing and Painting |
| 5361828 | Geometry |
| 5361830 | Earth and Space Science |
| 5361831 | Digital Imaging & Editing |
| 5361832 | English 10 Honors |
| 5361833 | English 10 Honors |
| 5361834 | Geometry |
| 5361835 | English 10 |
| 5361836 | Bible 10 |
| 5361838 | American Government & Politics |
| 5361840 | Spanish II |
| 5361842 | Bible 10 |
| 5361843 | Bible 10 |
| 5361844 | American Government & Politics Honors |
| 5361845 | Chorus - High  |
| 5361846 | Bible 10 |
| 5361847 | Earth and Space Science |
| 5361853 | English 10 Honors |
| 5361856 | English 10 |
| 5361857 | Alg II Honors |
| 5361858 | Chemistry Honors |
| 5361859 | Alg II Honors |
| 5361862 | Drawing and Painting |
| 5361863 | American Government & Politics |
| 5361864 | English 10 |
| 5361865 | English 10 |
| 5361867 | English 10 Honors |
| 5361868 | Algebra II |
| 5361869 | Bible 10 |
| 5361870 | American Government & Politics Honors |
| 5361871 | Spanish II |
| 5361872 | Algebra II |
| 5361873 | Drawing and Painting |
| 5361874 | American Literature Honors |
| 5361877 | Physics Honors |
| 5361878 | Physical Science |
| 5361879 | Financial Literacy |
| 5361880 | Anatomy & Physiology |
| 5361881 | Trig/PreCalculus |
| 5361882 | Studio Art II |
| 5361883 | Trig/Pre-Calculus Hon |
| 5361884 | Financial Literacy |
| 5361885 | American Literature Honors |
| 5361886 | Anatomy & Physiology |
| 5361887 | American Literature Honors |
| 5361888 | World History |
| 5361889 | Chemistry Honors |
| 5361890 | Studio Art I |
| 5361891 | Physical Science |
| 5361892 | American Literature |
| 5361893 | Drawing and Painting |
| 5361895 | American Literature |
| 5361896 | Bible 11 |
| 5361897 | Financial Literacy |
| 5361898 | Spanish III |
| 5361899 | Algebra II |
| 5361900 | World History |
| 5361901 | Health - High  |
| 5361902 | Alg II Honors |
| 5361903 | Bible 11 |
| 5361904 | Physical Education - High  |
| 5361905 | Anatomy & Physiology |
| 5361906 | Dual Enrollment English 151 |
| 5361907 | Dual Enrollment English 151 |
| 5361908 | Trig/PreCalculus |
| 5361909 | Bible 12 |
| 5361910 | Trig/Pre-Calculus Hon |
| 5361911 | Bible 12 |
| 5361912 | Dual Enrollment Intro. to Psych. 101 |
| 5361913 | Study Hall |
| 5361914 | Dual Enrollment Biology 101 |
| 5361915 | Chorus - High  |
| 5361917 | Graphic Design |
| 5361918 | Anatomy & Physiology |
| 5361919 | Dual Enrollment English 151 |
| 5361920 | Study Hall |
| 5361921 | Dual Enrollment English 151 |
| 5361922 | Dual Enrollment Biology 101 |
| 5361923 | Dual Enrollment Biology 101 |
| 5361924 | Anatomy & Physiology |
| 5361925 | Bible 12 |
| 5361926 | Trig/Algebra III |
| 5361927 | Drawing and Painting |
| 5361928 | Executive Internship I |
| 5361929 | Advanced Robotics |
| 5361930 | AP Calculus A/B |
| 5361932 | Dual Enrollment Biology 101 |
| 5361933 | Bible 12 |
| 5361934 | Health - High  |
| 5361935 | Dual Enrollment Biology 101 |
| 5361936 | Yearbook |
| 5361937 | Drawing and Painting |
| 5407480 | Dual Enrollment World Civ. 101 |
| 5407481 | US History |
| 5407488 | Digital Imaging & Editing |
| 5407494 | American Government & Politics Honors |
| 5407497 | English 10 |
| 5407498 | Trig/PreCalculus |
| 5407499 | Dual Enrollment World Civ. 101 |
| 5407500 | Drawing and Painting |
| 5407506 | Physical Science |
| 5407517 | English 10 Honors |
| 5407518 | Earth and Space Science |
| 5407519 | Broadcast Journalism |
| 5407520 | Spanish I |
| 5407527 | Dual Enrollment English 151 |
| 5407543 | Spanish II |
| 5407554 | English 10 |
| 5407556 | Alg II Honors |
| 5407560 | Digital Imaging & Editing |
| 5407561 | Bible 11 |
| 5407564 | Bible 12 |
| 5407584 | Health - High  |
| 5407593 | Financial Literacy |
| 5409913 | American Literature |
| 5424569 | Spanish II |
| 5424570 | Biology Honors |
| 5434946 | English 9 |
| 5439293 | English 9 |
| 5510555 | Biology Honors |
| 5593175 | Bible 12 |
| 5642283 | Algebra 1 |

### Block 2A

| Student ID | Course |
|------------|--------|
| 5361789 | Dual Enrollment English 151 |
| 5361796 | Bible 9 |
| 5361797 | English 9 Honors |
| 5361798 | Bible 9 |
| 5361799 | Graphic Design |
| 5361801 | Physical Education - High  |
| 5361802 | Health - High  |
| 5361803 | Band - High  |
| 5361804 | English 9 Honors |
| 5361806 | Studio Art I |
| 5361807 | English 9 |
| 5361808 | English 9 Honors |
| 5361810 | Health - High  |
| 5361813 | Algebra 1 Honors |
| 5361814 | US History |
| 5361816 | Physical Education - High  |
| 5361817 | Spanish I |
| 5361818 | Geometry Honors |
| 5361819 | US History |
| 5361820 | Health - High  |
| 5361821 | Geometry |
| 5361822 | US History |
| 5361825 | Geometry Honors |
| 5361827 | Spanish II |
| 5361828 | Bible 10 |
| 5361830 | American Government & Politics |
| 5361831 | Spanish II |
| 5361832 | Band - High  |
| 5361833 | Spanish I |
| 5361834 | Bible 10 |
| 5361835 | American Government & Politics |
| 5361836 | American Government & Politics |
| 5361838 | English 10 |
| 5361840 | Earth and Space Science |
| 5361842 | English 10 |
| 5361843 | Health - High  |
| 5361845 | Bible 10 |
| 5361846 | Chorus - High  |
| 5361847 | American Government & Politics |
| 5361851 | Alg II Honors |
| 5361853 | Bible 10 |
| 5361856 | Earth and Space Science |
| 5361857 | American Government & Politics Honors |
| 5361858 | Alg II Honors |
| 5361859 | Spanish II |
| 5361862 | American Government & Politics |
| 5361863 | Advanced Robotics |
| 5361864 | Earth and Space Science |
| 5361865 | Geometry |
| 5361867 | American Government & Politics Honors |
| 5361868 | American Government & Politics |
| 5361869 | English 10 |
| 5361870 | Band - High  |
| 5361871 | Algebra II |
| 5361872 | Bible 11 |
| 5361873 | Bible 11 |
| 5361874 | Band - High  |
| 5361876 | Dual Enrollment World Civ. 101 |
| 5361877 | Financial Literacy |
| 5361878 | Studio Art II |
| 5361879 | Modern America |
| 5361880 | Chemistry Honors |
| 5361881 | American Literature |
| 5361882 | Studio Art I |
| 5361883 | Studio Art I |
| 5361884 | Earth and Space Science |
| 5361885 | Marine Biology |
| 5361886 | Trig/PreCalculus |
| 5361887 | Dual Enrollment World Civ. 101 |
| 5361888 | Anatomy & Physiology |
| 5361889 | American Literature |
| 5361890 | Physical Science |
| 5361891 | Advanced Robotics |
| 5361892 | Algebra II |
| 5361893 | Algebra II |
| 5361895 | Bible 11 |
| 5361896 | Spanish II |
| 5361897 | Earth and Space Science |
| 5361898 | Dual Enrollment World Civ. 101 |
| 5361899 | Physical Science |
| 5361900 | Drawing and Painting |
| 5361901 | Spanish II |
| 5361902 | Spanish III |
| 5361903 | Physical Education - High  |
| 5361904 | Alg II Honors |
| 5361905 | American Literature Honors |
| 5361906 | Anatomy & Physiology |
| 5361908 | Graphic Design |
| 5361909 | Study Hall (Semester) |
| 5361910 | Dual Enrollment Biology 101 |
| 5361911 | Dual Enrollment World Civ. 151 |
| 5361912 | Dual Enrollment World Civ. 151 |
| 5361913 | Chemistry Honors |
| 5361914 | Dual Enrollment English 151 |
| 5361915 | Study Hall (Semester) |
| 5361917 | Marine Biology |
| 5361919 | Dual Enrollment Biology 101 |
| 5361920 | Recreational Sports |
| 5361921 | Bible 12 |
| 5361922 | Trig/PreCalculus |
| 5361923 | Band - High  |
| 5361924 | Statistics Honors |
| 5361925 | Dual Enrollment English 151 |
| 5361926 | Faith & Film |
| 5361927 | Health - High  |
| 5361928 | Bible 12 |
| 5361929 | Study Hall (Semester) |
| 5361930 | Recreational Sports |
| 5361932 | Dual Enrollment English 151 |
| 5361933 | World Literature |
| 5361934 | AP Computer Science |
| 5361935 | Bible 12 |
| 5361936 | Study Hall |
| 5361937 | World Literature |
| 5407480 | Digital Imaging & Editing |
| 5407481 | Algebra 1 Honors |
| 5407488 | Bible 10 |
| 5407494 | Alg II Honors |
| 5407497 | American Government & Politics |
| 5407498 | Marine Biology |
| 5407499 | Algebra II |
| 5407500 | Alg II Honors |
| 5407506 | Anatomy & Physiology |
| 5407517 | Chemistry Honors |
| 5407518 | Bible 10 |
| 5407519 | American Government & Politics |
| 5407520 | English 9 Honors |
| 5407527 | Trig/Algebra III |
| 5407543 | Bible 10 |
| 5407554 | Earth and Space Science |
| 5407556 | Chorus - High  |
| 5407560 | Earth and Space Science |
| 5407561 | Physical Science |
| 5407564 | Chorus - High  |
| 5407584 | Biology Honors |
| 5407593 | Trig/Pre-Calculus Hon |
| 5409913 | World History |
| 5419610 | Dual Enrollment English 151 |
| 5424569 | Alg II Honors |
| 5424570 | Digital Imaging & Editing |
| 5432621 | Trig/Algebra III |
| 5434946 | Bible 9 |
| 5439293 | Geometry |
| 5510555 | Spanish I |
| 5593175 | Dual Enrollment Biology 101 |
| 5642283 | Studio Art II |

### Block 2B

| Student ID | Course |
|------------|--------|
| 5361789 | Digital Imaging & Editing |
| 5361796 | Biology |
| 5361797 | Spanish I |
| 5361798 | English 9 |
| 5361799 | Bible 9 |
| 5361801 | Algebra 1 |
| 5361802 | Biology Honors |
| 5361803 | Biology |
| 5361804 | Geometry Honors |
| 5361806 | English 9 Honors |
| 5361807 | Bible 9 |
| 5361808 | Physical Education - High  |
| 5361810 | Bible 9 |
| 5361813 | Physical Education - High  |
| 5361814 | Spanish I |
| 5361816 | Geometry Honors |
| 5361817 | Algebra 1 |
| 5361818 | Biology Honors |
| 5361819 | Geometry Honors |
| 5361820 | Bible 9 |
| 5361821 | English 9 Honors |
| 5361822 | Health - High  |
| 5361825 | English 9 Honors |
| 5361827 | English 10 |
| 5361828 | English 10 |
| 5361830 | Bible 10 |
| 5361831 | English 10 |
| 5361832 | American Government & Politics Honors |
| 5361833 | Geometry |
| 5361834 | Earth and Space Science |
| 5361835 | Bible 10 |
| 5361836 | Earth and Space Science |
| 5361838 | Earth and Space Science |
| 5361840 | Bible 10 |
| 5361842 | Alg II Honors |
| 5361843 | Algebra II |
| 5361845 | English 10 |
| 5361846 | Spanish II |
| 5361847 | English 10 |
| 5361851 | American Government & Politics Honors |
| 5361853 | Studio Art II |
| 5361856 | American Government & Politics |
| 5361857 | Bible 10 |
| 5361858 | Spanish II |
| 5361859 | Bible 10 |
| 5361862 | Bible 10 |
| 5361863 | Earth and Space Science |
| 5361864 | Chorus - High  |
| 5361865 | Earth and Space Science |
| 5361867 | Spanish II |
| 5361868 | English 10 Honors |
| 5361869 | Alg II Honors |
| 5361870 | English 10 Honors |
| 5361871 | Health - High  |
| 5361872 | American Literature Honors |
| 5361873 | Alg II Honors |
| 5361874 | Dual Enrollment World Civ. 101 |
| 5361876 | Trig/Pre-Calculus Hon |
| 5361877 | Bible 11 |
| 5361878 | American Literature |
| 5361879 | Bible 11 |
| 5361880 | Drawing and Painting |
| 5361881 | Earth and Space Science |
| 5361882 | Trig/Pre-Calculus Hon |
| 5361883 | American Literature Honors |
| 5361884 | Bible 11 |
| 5361885 | Dual Enrollment Biology 101 |
| 5361886 | Bible 11 |
| 5361887 | Spanish I |
| 5361888 | Marine Biology |
| 5361889 | Bible 11 |
| 5361890 | World History |
| 5361891 | Digital Imaging & Editing |
| 5361892 | Bible 11 |
| 5361893 | Spanish II |
| 5361895 | Algebra II |
| 5361896 | World History |
| 5361897 | American Literature Honors |
| 5361898 | Trig/Pre-Calculus Hon |
| 5361899 | Digital Imaging & Editing |
| 5361900 | American Literature |
| 5361901 | American Literature |
| 5361902 | World History |
| 5361903 | Trig/Algebra III |
| 5361904 | American Literature |
| 5361905 | Marine Biology |
| 5361906 | Chorus - High  |
| 5361908 | Digital Imaging & Editing |
| 5361909 | Dual Enrollment English 151 |
| 5361910 | Study Hall |
| 5361911 | Trig/Pre-Calculus Hon |
| 5361912 | Bible 12 |
| 5361913 | Statistics Honors |
| 5361914 | Trig/PreCalculus |
| 5361915 | Executive Internship I |
| 5361917 | Personal Fitness |
| 5361918 | Bible 12 |
| 5361919 | Bible 12 |
| 5361920 | World Literature |
| 5361921 | Personal Fitness |
| 5361922 | Executive Internship I |
| 5361923 | Graphic Design |
| 5361924 | Study Hall |
| 5361925 | Study Hall |
| 5361926 | Study Hall |
| 5361927 | AP Computer Science |
| 5361928 | Dual Enrollment Biology 101 |
| 5361929 | World Literature |
| 5361930 | Bible 12 |
| 5361932 | Personal Fitness |
| 5361933 | Financial Literacy |
| 5361934 | Chemistry Honors |
| 5361935 | Dual Enrollment English 151 |
| 5361936 | AP Computer Science |
| 5361937 | Bible 12 |
| 5407480 | Biology Honors |
| 5407481 | English 9 |
| 5407488 | Spanish III |
| 5407494 | English 10 Honors |
| 5407497 | Earth and Space Science |
| 5407498 | Dual Enrollment English 151 |
| 5407499 | Drawing and Painting |
| 5407500 | Bible 11 |
| 5407506 | Bible 12 |
| 5407517 | Health - High  |
| 5407518 | Advanced Robotics |
| 5407519 | Drawing and Painting |
| 5407520 | US History |
| 5407527 | Dual Enrollment Intro. to Teaching 201 |
| 5407543 | Drawing and Painting |
| 5407554 | Bible 10 |
| 5407556 | Chemistry Honors |
| 5407560 | Bible 10 |
| 5407561 | Spanish II |
| 5407564 | Advanced Robotics |
| 5407584 | US History |
| 5407593 | Bible 11 |
| 5409913 | Digital Imaging & Editing |
| 5424569 | American Government & Politics |
| 5424570 | English 9 Honors |
| 5432621 | Biology Honors |
| 5434946 | Biology Honors |
| 5439293 | US History |
| 5510555 | Geometry Honors |
| 5593175 | Dual Enrollment English 151 |
| 5642283 | US History |

### Block 3

| Student ID | Course |
|------------|--------|
| 5361789 | AP Computer Science |
| 5361796 | Physical Education - High  |
| 5361797 | Bible 9 |
| 5361798 | US History |
| 5361799 | Biology Honors |
| 5361800 | Geometry |
| 5361801 | Bible 9 |
| 5361802 | Bible 9 |
| 5361803 | Algebra 1 |
| 5361804 | Health - High  |
| 5361806 | Bible 9 |
| 5361807 | Spanish I |
| 5361808 | US History |
| 5361810 | Spanish I |
| 5361811 | Geometry Honors |
| 5361812 | Geometry Honors |
| 5361813 | US History |
| 5361814 | Biology |
| 5361816 | English 9 Honors |
| 5361817 | Health - High  |
| 5361818 | Health - High  |
| 5361819 | English 9 |
| 5361820 | Biology |
| 5361821 | Biology |
| 5361822 | Geometry Honors |
| 5361825 | Spanish I |
| 5361827 | Bible 10 |
| 5361828 | American Government & Politics |
| 5361830 | Spanish II |
| 5361831 | American Government & Politics |
| 5361832 | Chemistry Honors |
| 5361833 | American Government & Politics |
| 5361834 | English 10 Honors |
| 5361835 | Spanish II |
| 5361836 | Spanish II |
| 5361838 | Algebra II |
| 5361840 | English 10 |
| 5361842 | American Government & Politics Honors |
| 5361843 | Spanish II |
| 5361845 | Algebra II |
| 5361846 | English 10 Honors |
| 5361847 | Alg II Honors |
| 5361851 | Chemistry Honors |
| 5361853 | Earth and Space Science |
| 5361856 | Bible 10 |
| 5361857 | Chemistry Honors |
| 5361858 | American Government & Politics Honors |
| 5361859 | English 10 Honors |
| 5361862 | Earth and Space Science |
| 5361863 | English 10 |
| 5361864 | Band - High  |
| 5361865 | Band - High  |
| 5361867 | Alg II Honors |
| 5361868 | Earth and Space Science |
| 5361869 | Band - High  |
| 5361870 | Alg II Honors |
| 5361871 | American Government & Politics |
| 5361872 | Spanish II |
| 5361873 | Anatomy & Physiology |
| 5361874 | Anatomy & Physiology |
| 5361877 | American Literature Honors |
| 5361878 | Studio Art I |
| 5361879 | Algebra II |
| 5361880 | Trig/Pre-Calculus Hon |
| 5361881 | World History |
| 5361882 | Dual Enrollment World Civ. 101 |
| 5361883 | Bible 11 |
| 5361884 | World History |
| 5361885 | Dual Enrollment World Civ. 101 |
| 5361886 | American Literature |
| 5361887 | Bible 11 |
| 5361888 | Algebra II |
| 5361889 | Trig/PreCalculus |
| 5361890 | Bible 11 |
| 5361891 | American Literature |
| 5361892 | Physical Science |
| 5361893 | Bible 11 |
| 5361895 | World History |
| 5361896 | American Literature |
| 5361897 | Dual Enrollment World Civ. 101 |
| 5361898 | Drawing and Painting |
| 5361899 | Bible 11 |
| 5361900 | Chemistry Honors |
| 5361901 | Bible 11 |
| 5361902 | Chemistry Honors |
| 5361903 | World History |
| 5361904 | World History |
| 5361905 | Bible 11 |
| 5361906 | Study Hall (Semester) |
| 5361908 | Study Hall |
| 5361909 | Study Hall |
| 5361910 | Executive Internship I |
| 5361911 | Study Hall |
| 5361912 | Study Hall |
| 5361913 | Bible 12 |
| 5361914 | Graphic Design |
| 5361915 | World Literature |
| 5361917 | Digital Imaging & Editing |
| 5361919 | American Literature Honors |
| 5361920 | Bible 12 |
| 5361921 | Recreational Sports |
| 5361922 | Dual Enrollment English 151 |
| 5361923 | Dual Enrollment English 151 |
| 5361924 | Dual Enrollment Intro. to Psych. 101 |
| 5361925 | Yearbook |
| 5361926 | Bible 12 |
| 5361927 | Study Hall |
| 5361928 | Dual Enrollment English 151 |
| 5361929 | Marine Biology |
| 5361930 | Band - High  |
| 5361932 | Trig/PreCalculus |
| 5361933 | Drawing and Painting |
| 5361934 | Bible 12 |
| 5361935 | Executive Internship II |
| 5361936 | Executive Internship II |
| 5361937 | Graphic Design |
| 5407480 | Algebra II |
| 5407481 | Graphic Design |
| 5407488 | Physical Science |
| 5407494 | Band - High  |
| 5407497 | Bible 10 |
| 5407498 | Bible 12 |
| 5407499 | Bible 11 |
| 5407500 | Dual Enrollment World Civ. 101 |
| 5407506 | Trig/Algebra III |
| 5407517 | Algebra II |
| 5407518 | American Government & Politics |
| 5407519 | Bible 10 |
| 5407520 | Biology Honors |
| 5407527 | Bible 12 |
| 5407543 | Earth and Space Science |
| 5407554 | Chorus - High  |
| 5407556 | Bible 11 |
| 5407560 | American Government & Politics |
| 5407561 | Financial Literacy |
| 5407564 | US History |
| 5407584 | Spanish I |
| 5407590 | Biology Honors |
| 5407593 | Chorus - High  |
| 5409913 | Graphic Design |
| 5424569 | Bible 11 |
| 5424570 | Geometry Honors |
| 5432621 | American Literature |
| 5434946 | Spanish I |
| 5439293 | Bible 9 |
| 5510555 | English 9 Honors |
| 5593175 | Spanish II |
| 5642283 | Bible 9 |

### Block 4A

| Student ID | Course |
|------------|--------|
| 5303312 | Bible 11 |
| 5361789 | Graphic Design |
| 5361796 | English 9 |
| 5361797 | Band - High  |
| 5361798 | Biology |
| 5361799 | Digital Imaging & Editing |
| 5361801 | English 9 |
| 5361802 | US History |
| 5361803 | English 9 |
| 5361804 | Biology Honors |
| 5361805 | Biology |
| 5361806 | Biology Honors |
| 5361807 | Health - High  |
| 5361808 | Geometry Honors |
| 5361810 | US History |
| 5361811 | Biology Honors |
| 5361812 | Biology Honors |
| 5361813 | Health - High  |
| 5361814 | Bible 9 |
| 5361816 | US History |
| 5361817 | Bible 9 |
| 5361818 | US History |
| 5361819 | Physical Education - High  |
| 5361820 | Algebra 1 |
| 5361822 | Physical Education - High  |
| 5361825 | Physical Education - High  |
| 5361827 | Earth and Space Science |
| 5361828 | Spanish II |
| 5361830 | English 10 |
| 5361831 | Bible 10 |
| 5361832 | Spanish II |
| 5361833 | Chemistry Honors |
| 5361834 | Spanish II |
| 5361835 | Earth and Space Science |
| 5361836 | English 10 |
| 5361838 | Spanish II |
| 5361840 | Geometry |
| 5361842 | Chemistry Honors |
| 5361843 | American Government & Politics |
| 5361844 | Chemistry Honors |
| 5361845 | Earth and Space Science |
| 5361846 | American Government & Politics Honors |
| 5361847 | Health - High  |
| 5361851 | English 10 Honors |
| 5361853 | American Government & Politics |
| 5361856 | Geometry |
| 5361857 | Spanish II |
| 5361858 | English 10 Honors |
| 5361859 | Chorus - High  |
| 5361862 | Algebra II |
| 5361863 | Geometry |
| 5361864 | Geometry |
| 5361865 | American Government & Politics |
| 5361867 | Band - High  |
| 5361868 | Bible 10 |
| 5361869 | American Government & Politics Honors |
| 5361870 | Bible 10 |
| 5361871 | Chemistry Honors |
| 5361872 | World History |
| 5361873 | Dual Enrollment World Civ. 101 |
| 5361874 | Marine Biology |
| 5361876 | American Literature Honors |
| 5361877 | Dual Enrollment World Civ. 101 |
| 5361878 | Algebra II |
| 5361879 | Chemistry Honors |
| 5361880 | World History |
| 5361881 | Bible 11 |
| 5361882 | American Literature Honors |
| 5361883 | Physics Honors |
| 5361884 | Algebra II |
| 5361885 | Bible 11 |
| 5361886 | Spanish III |
| 5361887 | Physics Honors |
| 5361888 | Spanish II |
| 5361889 | Spanish II |
| 5361890 | American Literature |
| 5361891 | Bible 11 |
| 5361892 | Chorus - High  |
| 5361893 | World History |
| 5361895 | Spanish II |
| 5361896 | Chemistry Honors |
| 5361897 | Dual Enrollment World Civ. 151 |
| 5361898 | Bible 11 |
| 5361899 | World History |
| 5361900 | Financial Literacy |
| 5361901 | Algebra II |
| 5361902 | Financial Literacy |
| 5361903 | Physical Science |
| 5361904 | Health - High  |
| 5361905 | Trig/Pre-Calculus Hon |
| 5361906 | Dual Enrollment Intro. to Psych. 101 |
| 5361907 | Trig/PreCalculus |
| 5361908 | World Literature |
| 5361909 | Spanish III |
| 5361910 | Bible 12 |
| 5361911 | Anatomy & Physiology |
| 5361912 | Chemistry Honors |
| 5361913 | Spanish III |
| 5361914 | Digital Imaging & Editing |
| 5361915 | Executive Internship II |
| 5361917 | Bible 12 |
| 5361918 | Dual Enrollment English 151 |
| 5361919 | Personal Fitness |
| 5361920 | Personal Fitness |
| 5361921 | Physics Honors |
| 5361922 | Study Hall |
| 5361923 | Bible 12 |
| 5361924 | Financial Literacy |
| 5361925 | Chorus - High  |
| 5361926 | Dual Enrollment Biology 101 |
| 5361927 | Bible 12 |
| 5361928 | Digital Imaging & Editing |
| 5361929 | Trig/Algebra III |
| 5361930 | Digital Imaging & Editing |
| 5361932 | Study Hall |
| 5361933 | Trig/Algebra III |
| 5361934 | World Literature |
| 5361935 | AP Calculus A/B |
| 5361936 | Bible 12 |
| 5361937 | Digital Imaging & Editing |
| 5407480 | Study Hall |
| 5407481 | Biology |
| 5407488 | Alg II Honors |
| 5407494 | Biology |
| 5407497 | Alg II Honors |
| 5407498 | Executive Internship I |
| 5407499 | Biology Honors |
| 5407500 | American Literature Honors |
| 5407506 | Executive Internship II |
| 5407517 | American Government & Politics Honors |
| 5407518 | Spanish II |
| 5407519 | Earth and Space Science |
| 5407520 | Geometry Honors |
| 5407527 | Dual Enrollment Intro. to Psych. 101 |
| 5407543 | American Government & Politics |
| 5407554 | American Government & Politics |
| 5407556 | Dual Enrollment World Civ. 101 |
| 5407560 | Spanish I |
| 5407561 | World History |
| 5407564 | Chemistry Honors |
| 5407584 | Bible 9 |
| 5407593 | US History |
| 5409913 | Biology |
| 5419610 | Trig/Algebra III |
| 5424569 | Health - High  |
| 5424570 | Bible 9 |
| 5432621 | Bible 11 |
| 5434946 | US History |
| 5439293 | Spanish I |
| 5510555 | Chorus - High  |
| 5593175 | Trig/Pre-Calculus Hon |
| 5642283 | Biology |

### Block 4B

| Student ID | Course |
|------------|--------|
| 5361789 | Bible 12 |
| 5361796 | Spanish I |
| 5361797 | Biology Honors |
| 5361798 | Physical Education - High  |
| 5361799 | Spanish I |
| 5361801 | US History |
| 5361802 | Geometry Honors |
| 5361803 | US History |
| 5361804 | Bible 9 |
| 5361806 | US History |
| 5361807 | Biology |
| 5361808 | Biology Honors |
| 5361809 | Bible 9 |
| 5361810 | English 9 Honors |
| 5361813 | Biology |
| 5361814 | English 9 |
| 5361816 | Bible 9 |
| 5361817 | Biology |
| 5361818 | English 9 |
| 5361819 | Bible 9 |
| 5361820 | US History |
| 5361822 | Biology Honors |
| 5361825 | US History |
| 5361827 | American Government & Politics |
| 5361828 | Earth and Space Science |
| 5361830 | Broadcast Journalism |
| 5361831 | Earth and Space Science |
| 5361832 | Alg II Honors |
| 5361833 | Chorus - High  |
| 5361834 | Drawing and Painting |
| 5361835 | Digital Imaging & Editing |
| 5361836 | Geometry |
| 5361838 | Digital Imaging & Editing |
| 5361840 | American Government & Politics |
| 5361842 | Health - High  |
| 5361843 | English 10 Honors |
| 5361844 | Alg II Honors |
| 5361845 | Spanish II |
| 5361846 | Alg II Honors |
| 5361847 | Spanish II |
| 5361851 | Bible 10 |
| 5361853 | Spanish II |
| 5361856 | Digital Imaging & Editing |
| 5361857 | Drawing and Painting |
| 5361858 | Band - High  |
| 5361859 | Chemistry Honors |
| 5361862 | Spanish II |
| 5361863 | Studio Art I |
| 5361864 | American Government & Politics |
| 5361865 | Spanish I |
| 5361867 | Chemistry Honors |
| 5361868 | Health - High  |
| 5361869 | Chemistry Honors |
| 5361870 | Chemistry Honors |
| 5361871 | Bible 10 |
| 5361872 | Band - High  |
| 5361873 | Marine Biology |
| 5361874 | Algebra II |
| 5361877 | Trig/Pre-Calculus Hon |
| 5361878 | Bible 11 |
| 5361879 | American Literature Honors |
| 5361880 | American Literature |
| 5361881 | Financial Literacy |
| 5361882 | Anatomy & Physiology |
| 5361883 | Dual Enrollment World Civ. 101 |
| 5361884 | American Literature |
| 5361885 | Spanish II |
| 5361886 | World History |
| 5361887 | Algebra II |
| 5361888 | Bible 11 |
| 5361889 | World History |
| 5361890 | Studio Art II |
| 5361891 | World History |
| 5361892 | Financial Literacy |
| 5361893 | American Literature |
| 5361895 | Physical Science |
| 5361896 | Digital Imaging & Editing |
| 5361897 | Trig/Pre-Calculus Hon |
| 5361898 | Chemistry Honors |
| 5361899 | Faith & Film |
| 5361900 | Bible 11 |
| 5361901 | Physical Science |
| 5361902 | Bible 11 |
| 5361903 | Spanish II |
| 5361904 | Physical Science |
| 5361905 | Spanish III |
| 5361906 | Bible 12 |
| 5361908 | Bible 12 |
| 5361909 | Digital Imaging & Editing |
| 5361910 | World Literature |
| 5361911 | Dual Enrollment English 151 |
| 5361912 | Dual Enrollment World Civ. 101 |
| 5361913 | Dual Enrollment English 151 |
| 5361914 | Bible 12 |
| 5361915 | Bible 12 |
| 5361917 | World Literature |
| 5361918 | Trig/Algebra III |
| 5361919 | Recreational Sports |
| 5361920 | Financial Literacy |
| 5361921 | Advanced Robotics |
| 5361922 | Yearbook |
| 5361923 | Digital Imaging & Editing |
| 5361924 | Dual Enrollment English 151 |
| 5361925 | Contemporary Issues |
| 5361926 | Dual Enrollment English 151 |
| 5361927 | Spanish III |
| 5361928 | Graphic Design |
| 5361929 | Bible 12 |
| 5361930 | Personal Fitness |
| 5361932 | Recreational Sports |
| 5361933 | Study Hall |
| 5361934 | Study Hall |
| 5361935 | Dual Enrollment Chemistry 105 |
| 5361936 | World Literature |
| 5361937 | Physics Honors |
| 5407480 | Bible 11 |
| 5407481 | Digital Imaging & Editing |
| 5407488 | English 10 Honors |
| 5407494 | Bible 10 |
| 5407497 | Spanish II |
| 5407498 | Dual Enrollment Biology 101 |
| 5407499 | Spanish II |
| 5407500 | Spanish II |
| 5407506 | World Literature |
| 5407517 | Bible 10 |
| 5407518 | Geometry |
| 5407519 | Algebra II |
| 5407520 | Bible 9 |
| 5407527 | US History |
| 5407543 | English 10 |
| 5407554 | Spanish I |
| 5407556 | Digital Imaging & Editing |
| 5407560 | Graphic Design |
| 5407561 | American Literature |
| 5407564 | Dual Enrollment English 151 |
| 5407584 | Algebra 1 |
| 5407590 | Geometry Honors |
| 5407593 | Chemistry Honors |
| 5409913 | Algebra II |
| 5419610 | Bible 12 |
| 5424569 | American Literature Honors |
| 5424570 | US History |
| 5432621 | American Government & Politics |
| 5434946 | Geometry |
| 5439293 | Biology |
| 5510555 | Bible 9 |
| 5593175 | Journalism |
| 5642283 | Studio Art I |


## Teachers Block-wise View

This view shows all teachers assigned to each block.

### Block 1A

| Teacher ID | Course | Number of Students |
|------------|--------|-------------------|

### Block 1B

| Teacher ID | Course | Number of Students |
|------------|--------|-------------------|

### Block 2A

| Teacher ID | Course | Number of Students |
|------------|--------|-------------------|

### Block 2B

| Teacher ID | Course | Number of Students |
|------------|--------|-------------------|

### Block 3

| Teacher ID | Course | Number of Students |
|------------|--------|-------------------|

### Block 4A

| Teacher ID | Course | Number of Students |
|------------|--------|-------------------|

### Block 4B

| Teacher ID | Course | Number of Students |
|------------|--------|-------------------|


## Sample Individual Student Schedules

### Student 5407488

| Block | Course |
|-------|--------|
| 1A | American Government & Politics |
| 1B | Digital Imaging & Editing |
| 2A | Bible 10 |
| 2B | Spanish III |
| 3 | Physical Science |
| 4A | Alg II Honors |
| 4B | English 10 Honors |

### Student 5361799

| Block | Course |
|-------|--------|
| 1A | US History |
| 1B | English 9 |
| 2A | Graphic Design |
| 2B | Bible 9 |
| 3 | Biology Honors |
| 4A | Digital Imaging & Editing |
| 4B | Spanish I |

### Student 5361901

| Block | Course |
|-------|--------|
| 1A | World History |
| 1B | Health - High  |
| 2A | Spanish II |
| 2B | American Literature |
| 3 | Bible 11 |
| 4A | Algebra II |
| 4B | Physical Science |

### Student 5361882

| Block | Course |
|-------|--------|
| 1A | Bible 11 |
| 1B | Studio Art II |
| 2A | Studio Art I |
| 2B | Trig/Pre-Calculus Hon |
| 3 | Dual Enrollment World Civ. 101 |
| 4A | American Literature Honors |
| 4B | Anatomy & Physiology |

### Student 5361922

| Block | Course |
|-------|--------|
| 1A | Bible 12 |
| 1B | Dual Enrollment Biology 101 |
| 2A | Trig/PreCalculus |
| 2B | Executive Internship I |
| 3 | Dual Enrollment English 151 |
| 4A | Study Hall |
| 4B | Yearbook |


## Sample Individual Teacher Schedules

