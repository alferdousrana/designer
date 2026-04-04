import { useEffect, useState } from "react";
import {
  getFeaturedBlogs,
  getFeaturedProjects,
  getHomePageData,
} from "../services/api/homeApi";
import {
  mockFeaturedBlogs,
  mockFeaturedProjects,
  mockHomeData,
} from "../data/mockHomeData";

function useHomeData() {
  const [homeData, setHomeData] = useState(mockHomeData);
  const [featuredProjects, setFeaturedProjects] = useState(mockFeaturedProjects);
  const [featuredBlogs, setFeaturedBlogs] = useState(mockFeaturedBlogs);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadHomeData() {
      try {
        setLoading(true);
        setError("");

        const [homeResponse, projectResponse, blogResponse] = await Promise.all([
          getHomePageData(),
          getFeaturedProjects(),
          getFeaturedBlogs(),
        ]);

        setHomeData(homeResponse || mockHomeData);

        setFeaturedProjects(
          Array.isArray(projectResponse)
            ? projectResponse
            : projectResponse?.results || mockFeaturedProjects
        );

        setFeaturedBlogs(
          Array.isArray(blogResponse)
            ? blogResponse
            : blogResponse?.results || mockFeaturedBlogs
        );
      } catch (err) {
        console.error(err);
        setError("Failed to load API data. Showing fallback content.");
        setHomeData(mockHomeData);
        setFeaturedProjects(mockFeaturedProjects);
        setFeaturedBlogs(mockFeaturedBlogs);
      } finally {
        setLoading(false);
      }
    }

    loadHomeData();
  }, []);

  return {
    homeData,
    featuredProjects,
    featuredBlogs,
    loading,
    error,
  };
}

export default useHomeData;