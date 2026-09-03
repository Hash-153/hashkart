import React, { createContext, useContext, useState, useEffect } from 'react';
import { User } from '../types';
import { api } from '../services/api';

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (token: string, refreshToken?: string) => Promise<void>;
  logout: () => Promise<void>;
  refreshUser: () => Promise<void>;
  isAdmin: boolean;
  isManager: boolean;
  isStaff: boolean;
  hasRole: (roleName: string) => boolean;
  hasPermission: (permissionCode: string) => boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  const fetchUser = async () => {
    const token = localStorage.getItem('novamart_token');
    if (!token) {
      setUser(null);
      setLoading(false);
      return;
    }
    try {
      const u = await api.getMe();
      setUser(u);
    } catch (err) {
      console.error('Failed to fetch current user profile:', err);
      localStorage.removeItem('novamart_token');
      localStorage.removeItem('novamart_refresh_token');
      setUser(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUser();
  }, []);

  const login = async (token: string, refreshToken?: string) => {
    localStorage.setItem('novamart_token', token);
    if (refreshToken) {
      localStorage.setItem('novamart_refresh_token', refreshToken);
    }
    await fetchUser();
  };

  const logout = async () => {
    try {
      await api.logout();
    } catch {
      // Ignore network failures on logout
    } finally {
      localStorage.removeItem('novamart_token');
      localStorage.removeItem('novamart_refresh_token');
      setUser(null);
    }
  };

  const hasRole = (roleName: string): boolean => {
    if (!user) return false;
    if (user.roles.includes('ADMIN')) return true;
    return user.roles.includes(roleName);
  };

  const hasPermission = (permissionCode: string): boolean => {
    if (!user) return false;
    if (user.roles.includes('ADMIN')) return true;
    return (user.permissions || []).includes(permissionCode);
  };

  const isAdmin = hasRole('ADMIN');
  const isManager = hasRole('MANAGER');
  const isStaff = hasRole('STAFF') || hasRole('SUPPORT');

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        login,
        logout,
        refreshUser: fetchUser,
        isAdmin,
        isManager,
        isStaff,
        hasRole,
        hasPermission,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
