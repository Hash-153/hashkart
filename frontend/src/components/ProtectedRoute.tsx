import React from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

interface ProtectedRouteProps {
  children: React.ReactNode;
  allowedRoles?: string[];
  requiredPermission?: string;
}

export const ProtectedRoute: React.FC<ProtectedRouteProps> = ({
  children,
  allowedRoles,
  requiredPermission,
}) => {
  const { user, loading, hasRole, hasPermission } = useAuth();
  const location = useLocation();

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="w-12 h-12 border-4 border-blue-600 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-gray-600 font-medium">Verifying security session...</p>
        </div>
      </div>
    );
  }

  if (!user) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  if (allowedRoles && allowedRoles.length > 0) {
    const hasAnyRole = allowedRoles.some((role) => hasRole(role));
    if (!hasAnyRole) {
      return (
        <div className="max-w-4xl mx-auto py-16 px-4 text-center">
          <div className="bg-red-50 border border-red-200 rounded-xl p-8 max-w-lg mx-auto shadow-sm">
            <span className="text-4xl mb-4 block">🚫</span>
            <h2 className="text-2xl font-bold text-red-700 mb-2">Access Denied</h2>
            <p className="text-gray-600 mb-6">
              Your current account role does not have permission to view this administrative resource.
            </p>
            <a
              href="/"
              className="inline-block bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2.5 rounded-lg transition-colors shadow"
            >
              Return to Storefront
            </a>
          </div>
        </div>
      );
    }
  }

  if (requiredPermission && !hasPermission(requiredPermission)) {
    return (
      <div className="max-w-4xl mx-auto py-16 px-4 text-center">
        <div className="bg-red-50 border border-red-200 rounded-xl p-8 max-w-lg mx-auto shadow-sm">
          <span className="text-4xl mb-4 block">🔒</span>
          <h2 className="text-2xl font-bold text-red-700 mb-2">Permission Restricted</h2>
          <p className="text-gray-600 mb-6">
            Required permission code: <code className="bg-red-100 text-red-800 px-2 py-0.5 rounded font-mono text-sm">{requiredPermission}</code>
          </p>
          <a
            href="/"
            className="inline-block bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2.5 rounded-lg transition-colors shadow"
          >
            Return to Storefront
          </a>
        </div>
      </div>
    );
  }

  return <>{children}</>;
};
